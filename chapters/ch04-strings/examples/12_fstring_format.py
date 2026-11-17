# file: examples/12_fstring_format.py
items = [("Chai", 80, 3), ("Biryani", 450, 2), ("Kheer", 150, 1)]

print(f"{'Item':<10}{'Rate':>8}{'Qty':>5}{'Total':>10}")
print("-" * 33)
for name, rate, qty in items:
    print(f"{name:<10}{rate:>8,}{qty:>5}{rate * qty:>10,.2f}")
print("-" * 33)

print(f"[{'MIAVRO':^14}]")
print(f"[{'MIAVRO':*^14}]")
print(f"Invoice #{7:05d}")
print(f"{0.4567:.1%} | {1234567.891:,.2f} | {255:b} | {255:x} | {0.000123:.2e}")

width = 12
print(f"[{'dynamic':>{width}}]")      # width bhi variable se
