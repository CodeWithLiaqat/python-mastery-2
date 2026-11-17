# file: solutions/ex03_largest.py
a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

if a >= b and a >= c:
    largest = a
elif b >= c:
    largest = b
else:
    largest = c
print("Sab se bara:", largest)
