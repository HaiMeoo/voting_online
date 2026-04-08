# Online Voting System for Elections
 It is a desktop application made with socket programming in Python. 
 It uses synchronous multithreading. 
 

# Requirements

Python Libraries Required :

➔ Pandas

➔ Tkinter

➔ Socket

➔ Subprocess


# Tools Used


➢ Programming : Python

➢ Connection : Socket Programming

➢ Protocol : TCP

➢ User Interface : python-tkinter

➢ Data Storage : Using CSV files

➢ Data Updates : python-pandas

➢ OS Calls : python-subprocess


# How to Run

1. Open terminal/command prompt on your PC.

2. Navigate to ‘Voting’ folder

3. Run command : "python homePage.py"

4. A new home page window should open. If this doesn’t happen, check your installations.

5. Login into Admin using given details in ‘How to Login’ part.

6. Click on the ‘Run Server’ Button.

7. Use the rest of the Buttons as per your need.


# How to Login

❖ Admin Login :

➔ Admin ID : Admin

➔ Password : admin



❖ Voter Login:

❏ Server should be running for voters to be able to login.

➔ Already registered voter I.Ds : 10001 to 10005

➔ Password (for already registered voters) : abcd


# Workflow Description

❖ Inorder Description to run & test this project :

1. Open terminal & run python homePage.py to open Home Page Window.

2. Log into Admin and press ‘Run Server’. This will run the Server in a new console window.

3. Now that the server is running, return to the admin home page window.

4. Press ‘Register Voter’ and enter details to register a new voter. Remember or note down the ‘Voter ID’ that you will receive on successful registration.

5. Press ‘Home’ to return to the Home. Now, press ‘Voter Login’ to open the voter login page.

6. Enter the login details and you are redirected to the Voting Page. You will receive an error message if the Voter is invalid or has already cast a vote.

7. Cast a Vote. Now on receiving a success message, press home to return to home.

8. Login into Admin again. Press ‘Show Votes’ to check the votes that all parties have received so far.

9. Return to Home. You can press ‘New Window’ to open multiple pages and cast a vote concurrently from multiple voters.



## Stepwise Output / Test Cases

![image-001](https://github.com/webricated/voting-system-python/assets/105015109/6f34b001-0927-40bf-a801-b5d615c2aefa)


Home Page




![image-002](https://github.com/webricated/voting-system-python/assets/105015109/e68f56aa-4841-4ce1-be16-aa219bfa30e3)


Admin Login




![image-003](https://github.com/webricated/voting-system-python/assets/105015109/94f92ca4-af7d-4c34-87a0-b8c0289771c0)


Admin Home




![image-004](https://github.com/webricated/voting-system-python/assets/105015109/9a5005eb-6895-42c5-a6f1-de79e47eae7a)


Register Voter




![image-005](https://github.com/webricated/voting-system-python/assets/105015109/6daba5d9-35fc-4f02-a645-84771a1e1e36)


Register Success Message




![image-006](https://github.com/webricated/voting-system-python/assets/105015109/dc5cebbc-1fc7-4e88-b543-ee866a47cd5b)


Voter Login





# Test Case 1 : If detail matches, then it welcomes the voter and displays the name and poll symbol of the candidates


![image-007](https://github.com/webricated/voting-system-python/assets/105015109/93a0d0bb-dcdc-4fea-8f77-9dec4241382c)


Voting Page




![image-008](https://github.com/webricated/voting-system-python/assets/105015109/2fafd9f1-71a1-45c0-8ba0-c71f76363c69)


Vote Casted Successfully Message




![image-009](https://github.com/webricated/voting-system-python/assets/105015109/b0abb3e4-e4cd-4f1b-bdaf-938fa0c4975d)


Show Votes





❖ Error Handling :


# Test Case 2 : One client can cast a vote ONCE AND ONLY ONCE.


![image-010](https://github.com/webricated/voting-system-python/assets/105015109/3cf0f321-bd82-4f09-b2b7-ae9c4ddffb30)


If the vote already been casted




![image-011](https://github.com/webricated/voting-system-python/assets/105015109/35dc3c85-fad3-49e2-b97d-3de741346b0a)


# If a voter is not registered/invalid voter




![image-012](https://github.com/webricated/voting-system-python/assets/105015109/191af758-b9a2-43a6-ac73-bba0d3316d2d)


Error while casting vote





❖ Voters casting vote concurrently :


# Test Case 3: This system should work perfectly for at least 5 different clients at the same time.

![image-013](https://github.com/webricated/voting-system-python/assets/105015109/0a72652c-614d-4ddf-8e3e-7d08c1b45a29)


6 Voters




# Server Output


![image-014](https://github.com/webricated/voting-system-python/assets/105015109/aedb2747-996c-4c76-aad3-edad9f7a0c2c)


# Database




![image-015](https://github.com/webricated/voting-system-python/assets/105015109/5d4f74f1-d724-4d34-bd6c-6c8dda157f53)


Voter Info Database




![image-016](https://github.com/webricated/voting-system-python/assets/105015109/6bf5ed48-3cdb-4935-bd7e-f42a47e4f2b7)



Candidate Info Database





## Conclusion


For the ‘E-voting system’ project we learned how to implement TCP socket programming using Python. We also learned how to connect multiple clients with one server . As the requirement of the project was to allocate a new thread by server for every new incoming Client,thus to accomplish this requirement we learned how to implement synchronized multithreading in python and implemented it in the code of socket programming.




## Flow Chart


![img173](https://github.com/webricated/voting-system-python/assets/105015109/2fd77c27-935b-49c3-ae8f-bd1500af4e1f)







