# file: examples/04_range.py
for i in range(5):
    print(i, end=" ")
print()

for i in range(1, 11, 3):
    print(i, end=" ")
print()

for i in range(5, 0, -1):
    print(i, end="... ")
print("Liftoff!")

print(list(range(2, 12, 2)))
