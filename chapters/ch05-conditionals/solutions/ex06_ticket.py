# file: solutions/ex06_ticket.py
age = int(input("Umar: "))
is_weekend = input("Weekend hai? (haan/nahi): ").strip().lower() == "haan"

if age <= 3:
    price = 0
elif age <= 12:
    price = 400
elif age <= 59:
    price = 800
else:
    price = 500

if is_weekend and price > 0:
    price *= 1.20

print(f"Ticket: {price:,.0f} PKR")
