# file: examples/05_logical.py
age = 20
has_cnic = True
balance = 0

can_open_account = age >= 18 and has_cnic
print("Account khul sakta hai?", can_open_account)

is_weekend = False
is_holiday = True
print("Chhutti?", is_weekend or is_holiday)

print("Balance khaali nahi?", not balance == 0)

# Short-circuit evaluation
x = 0
print(x != 0 and 10 / x > 1)   # pehli condition False, doosri chali hi nahi
