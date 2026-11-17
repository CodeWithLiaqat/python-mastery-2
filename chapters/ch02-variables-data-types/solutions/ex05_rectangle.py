# file: solutions/ex05_rectangle.py
length = float(input("Length (m): "))
width = float(input("Width (m): "))

area = length * width
perimeter = 2 * (length + width)

print(f"Area: {area:.2f} sq m")
print(f"Perimeter: {perimeter:.2f} m")
