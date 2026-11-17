# file: examples/11_electricity_slabs.py
units = int(input("Units istemal: "))

if units <= 100:
    bill = units * 10
elif units <= 200:
    bill = 100 * 10 + (units - 100) * 15
else:
    bill = 100 * 10 + 100 * 15 + (units - 200) * 22

surcharge = bill * 0.05 if units > 300 else 0
total = bill + surcharge

print(f"Bill     : {bill:,.2f}")
print(f"Surcharge: {surcharge:,.2f}")
print(f"Total    : {total:,.2f}")
