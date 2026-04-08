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


def ensure_current_account_session(address):
    address = address.lower()
    last_address = session.get("last_voted_address")
    if last_address != address:
        session["last_voted_address"] = address
        session["address_has_voted"] = False


def has_current_address_voted():
    return session.get("address_has_voted", False)


def set_current_address_voted():
    session["address_has_voted"] = True


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


def update_vote_count(name):
    df = pd.read_csv(FILE_PATH)
    if name not in df["Name"].values:
        return False

    df["Vote Count"] = df["Vote Count"].astype(int)
    df.loc[df["Name"] == name, "Vote Count"] += 1
    df.to_csv(FILE_PATH, index=False)
    return True


# =========================
# Route vote (ghi dữ liệu vào CSV)
# =========================
@app.route("/vote", methods=["POST"])
def vote():
    if request.is_json:
        data = request.get_json()
        name = data.get("candidate")
        address = data.get("address")
    else:
        name = request.form.get("candidate")
        address = request.form.get("address")

    if not name or not address:
        if request.is_json:
            return jsonify({"success": False, "error": "Candidate and address are required"}), 400
        flash("❌ Không tìm thấy ứng viên hoặc địa chỉ ví.", "error")
        return redirect("/vote_page")

    address = address.lower()
    ensure_current_account_session(address)
    if has_current_address_voted():
        if request.is_json:
            return jsonify({"success": False, "error": "Account này đã vote rồi."}), 400
        flash("❌ Account này đã vote rồi.", "error")
        return redirect("/vote_page")

    success = update_vote_count(name)
    if not success:
        if request.is_json:
            return jsonify({"success": False, "error": f"Không tìm thấy ứng viên {name}."}), 400
        flash(f"❌ Không tìm thấy ứng viên {name}.", "error")
        return redirect("/vote_page")

    set_current_address_voted()

    if request.is_json:
        return jsonify({"success": True})

    flash(f"✅ Vote cho {name} đã được lưu lại.", "success")
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