# file: solutions/ex07_fixed.py
import math

total_marks = 450
obtained = 380
percentage = obtained / total_marks * 100
print(f"Percentage: {percentage:.2f}")
print(round(percentage, 2) == 84.44)
print(math.isclose(percentage, 84.44, abs_tol=0.01))

city = "Quetta"
print(city in ("Lahore", "Karachi"))
