# file: examples/12_bill_splitter.py
# Mini Project 1: Bill Splitter + Tip Calculator
import math

print("=" * 38)
print("      BILL SPLITTER + TIP CALCULATOR")
print("=" * 38)

bill = float(input("Bill ki raqam (PKR): "))
tip_percent = float(input("Tip kitne percent? "))
people = int(input("Kitne log? "))

tip = bill * tip_percent / 100
total = bill + tip
exact_share = total / people
rounded_share = math.ceil(exact_share)         # upar ki taraf round
collected = rounded_share * people
extra = collected - total

print("-" * 38)
print(f"Bill          : PKR {bill:>12,.2f}")
print(f"Tip ({tip_percent:.0f}%)     : PKR {tip:>12,.2f}")
print(f"Total         : PKR {total:>12,.2f}")
print("-" * 38)
print(f"Har aik ka hissa (exact) : {exact_share:,.2f}")
print(f"Har aik dega (rounded)   : {rounded_share:,}")
print(f"Jama hoga                : {collected:,}")
print(f"Extra (waiter ke liye)   : {extra:,.2f}")
print("=" * 38)
