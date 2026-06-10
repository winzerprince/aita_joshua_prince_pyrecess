credentials = {"username": "winzer", "password": "pass"}

username = input("Enter username\n")
password = input("Enter password\n")

if username == credentials["username"]:
    if password == credentials["password"]:
        print(f"Correct credentials, welcome back {username}")

    else:
        print("Wrong password")
else:
    print("Wrong username")
