# file: solutions/ex04_login.py
USERNAME = "admin"
PASSWORD = "miavro123"

user = input("Username: ").strip()
pwd = input("Password: ")

if user != USERNAME:
    print("Username ghalat hai.")
elif pwd != PASSWORD:
    print("Password ghalat hai.")
else:
    print("Login kamyab!")
