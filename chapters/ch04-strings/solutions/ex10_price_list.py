# file: solutions/ex10_price_list.py
p1, price1 = "Basmati Rice", 1850.0
p2, price2 = "Cooking Oil", 2675.5
p3, price3 = "Tea 950g", 1399.0
total = price1 + price2 + price3

print("=" * 27)
print(f"{'PRICE LIST':^27}")
print("=" * 27)
print(f"{p1:<15}{price1:>12,.2f}")
print(f"{p2:<15}{price2:>12,.2f}")
print(f"{p3:<15}{price3:>12,.2f}")
print("-" * 27)
print(f"{'TOTAL':<15}{total:>12,.2f}")
