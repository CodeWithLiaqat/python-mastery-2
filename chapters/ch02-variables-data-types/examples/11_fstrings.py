# file: examples/11_fstrings.py
name = "Bilal"
price = 1499.5
quantity = 3
salary = 185000
score = 0.8765

print(f"Customer: {name}")
print(f"Total: {price * quantity} PKR")              # expression bhi chalta hai
print(f"Qeemat: {price:.2f} PKR")                     # 2 decimal places
print(f"Salary: {salary:,} PKR")                      # hazaron ka comma
print(f"Score: {score:.1%}")                          # percentage
print(f"Bara naam: {name.upper()}")                    # method call bhi ho sakti hai
print(f"{price = }")                                  # debugging shortcut (3.8+)
