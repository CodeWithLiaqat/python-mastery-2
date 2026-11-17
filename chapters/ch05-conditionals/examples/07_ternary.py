# file: examples/07_ternary.py
age = 16
status = "Adult" if age >= 18 else "Minor"
print(status)

marks = 45
print(f"Natija: {'Pass' if marks >= 50 else 'Fail'}")

items = 1
print(f"{items} item{'s' if items != 1 else ''}")

fee = 0 if age < 12 else (500 if age < 60 else 250)
print("Ticket:", fee)
