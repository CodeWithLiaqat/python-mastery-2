# file: solutions/ex09_triangle.py
a = float(input("Side a: "))
b = float(input("Side b: "))
c = float(input("Side c: "))

if a + b <= c or a + c <= b or b + c <= a:
    print("Yeh triangle nahi ban sakta.")
elif a == b == c:
    print("Equilateral")
elif a == b or b == c or a == c:
    print("Isosceles")
else:
    print("Scalene")
