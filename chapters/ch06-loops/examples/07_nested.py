# file: examples/07_nested.py
# Multiplication table (1-4) ka grid
for row in range(1, 5):
    for col in range(1, 5):
        print(f"{row * col:4}", end="")
    print()

print()
# Star pattern
for i in range(1, 5):
    print("*" * i)
