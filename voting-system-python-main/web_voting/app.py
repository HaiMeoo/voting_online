from flask import Flask, render_template, request, redirect, session, flash, jsonify
from eth_account.messages import encode_defunct
import pandas as pd
import os

app = Flask(__name__)
app.secret_key = "123456"

# Đường dẫn file CSV
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(BASE_DIR, "../database/cand_list.csv")


# =========================
# Đọc danh sách ứng viên
# =========================
def get_candidates():
    df = pd.read_csv(FILE_PATH)
    return df


# =========================
# Trang đăng nhập
# =========================
@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        session["user"] = request.form["username"]
        return redirect("/vote_page")
    return render_template("login.html")


# =========================
# Trang vote
# =========================
@app.route("/vote_page")
def vote_page():
    if "user" not in session:
        return redirect("/")

    df = get_candidates()
    return render_template("vote.html", candidates=df.to_dict(orient="records"))


# =========================
# Route vote (KHÔNG gọi blockchain nữa)
# =========================
@app.route("/vote", methods=["POST"])
def vote():
    name = request.form["candidate"]

    # Chỉ thông báo (vote thật xử lý bằng MetaMask JS)
    flash(f"🟡 Đã gửi yêu cầu vote cho {name} (xác nhận trên MetaMask)", "info")

    return redirect("/vote_page")


# =========================
# Trang kết quả
# =========================
@app.route("/result")
def result():
    df = get_candidates()

    # Hiện dữ liệu từ CSV (tạm thời)
    candidates = df.to_dict(orient="records")

    return render_template("result.html", candidates=candidates)


# =========================
# Đăng nhập bằng MetaMask
# =========================
@app.route('/login_wallet', methods=['POST'])
def login_wallet():
    data = request.get_json()

    address = data.get("address")
    signature = data.get("signature")
    message = data.get("message")

    try:
        msg = encode_defunct(text=message)
        recovered_address = encode_defunct

        # NOTE: đoạn này giữ lại để bạn mở rộng sau
        session["user"] = address
        return jsonify({"success": True})

    except Exception as e:
        print("Lỗi verify:", e)
        return jsonify({"success": False})
@app.route("/reset")
def reset():
    df = pd.read_csv(FILE_PATH)
    df["Vote Count"] = 0
    df.to_csv(FILE_PATH, index=False)

    return "Đã reset dữ liệu!"

# =========================
# Run app
# =========================
if __name__ == "__main__":
    app.run(debug=True)