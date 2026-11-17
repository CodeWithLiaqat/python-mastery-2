# file: examples/12_multiple_assignment.py
# Aik line mein kai variables
x, y, z = 10, 20, 30
print(x, y, z)

# Sab ko aik hi value
a = b = c = 0
print(a, b, c)

# Swapping: Python ka khoobsurat tareeqa
first = "Chai"
second = "Coffee"
first, second = second, first
print(f"first = {first}, second = {second}")

# Constants: UPPER_CASE convention
GST_RATE = 0.18
MAX_STUDENTS = 40
bill = 5000
print(f"GST: {bill * GST_RATE} PKR")
