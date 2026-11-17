# file: solutions/ex08_receipt_v2.py
# Chai Dhaba Receipt 2.0
CHAI_PRICE = 80
PARATHA_PRICE = 60
OMELETTE_PRICE = 150
SERVICE_RATE = 0.05

chai_qty = int(input("Chai kitni? "))
paratha_qty = int(input("Paratha kitne? "))
omelette_qty = int(input("Omelette kitne? "))

chai_total = chai_qty * CHAI_PRICE
paratha_total = paratha_qty * PARATHA_PRICE
omelette_total = omelette_qty * OMELETTE_PRICE
subtotal = chai_total + paratha_total + omelette_total
service = subtotal * SERVICE_RATE
grand_total = subtotal + service

print("===== Bismillah Chai Dhaba =====")
print(f"Chai     x{chai_qty} : {chai_total:,} PKR")
print(f"Paratha  x{paratha_qty} : {paratha_total:,} PKR")
print(f"Omelette x{omelette_qty} : {omelette_total:,} PKR")
print("--------------------------------")
print(f"Subtotal    : {subtotal:,} PKR")
print(f"Service 5%  : {service:,.2f} PKR")
print(f"Kul Bill    : {grand_total:,.2f} PKR")
