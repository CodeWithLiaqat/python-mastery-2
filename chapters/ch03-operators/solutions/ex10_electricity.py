# file: solutions/ex10_electricity.py
import math

TAX_RATE = 0.17
units = int(input("Units: "))
rate = float(input("Rate per unit (PKR): "))

base = units * rate
total = math.ceil(base * (1 + TAX_RATE))
notes, change = divmod(total, 500)

print(f"Base bill   : {base:,.2f}")
print(f"Tax ke saath: {total:,}")
print(f"500 ke {notes} note, baqi {change} PKR")
