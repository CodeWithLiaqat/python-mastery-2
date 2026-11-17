# file: examples/10_float_precision.py
print(0.1 + 0.2)
print(0.1 + 0.2 == 0.3)

# Sahi tareeqa 1: display ke liye format
print(f"{0.1 + 0.2:.2f}")

# Sahi tareeqa 2: muqable ke liye math.isclose
import math
print(math.isclose(0.1 + 0.2, 0.3))

# round(): banker's rounding
print(round(3.14159, 2))
print(round(2.5), round(3.5), round(0.5))
print(round(1234567, -3))        # hazar tak round
