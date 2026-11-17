# file: solutions/ex01_table.py
n = int(input("Number: "))
for i in range(1, 11):
    print(f"{n} x {i:>2} = {n * i:>3}")
