# file: solutions/ex08_password.py
CORRECT = "pak@1947"
MAX_TRIES = 3

for attempt in range(1, MAX_TRIES + 1):
    pwd = input("Password: ")
    if pwd == CORRECT:
        print("Login kamyab!")
        break
    remaining = MAX_TRIES - attempt
    if remaining:
        print(f"  Ghalat. {remaining} koshish baqi.")
else:
    print("Account locked. Customer support se rabta karein.")
