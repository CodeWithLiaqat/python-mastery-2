# file: examples/06_truthiness.py
name = ""
items = []
discount = 0
user = None

if name:
    print(f"Hello {name}")
else:
    print("Naam khaali hai")

if not items:
    print("Cart khaali hai")

if discount:
    print("Discount laga")
else:
    print("Koi discount nahi")

if user is None:
    print("Login nahi hua")
