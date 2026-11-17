# file: solutions/ex08_bmi.py
weight = float(input("Wazan (kg): "))
height = float(input("Qad (m): "))

if weight <= 0 or height <= 0:
    print("Wazan aur qad zero se zyada hone chahiye.")
else:
    bmi = weight / height ** 2
    if bmi < 18.5:
        category = "Underweight"
    elif bmi < 25:
        category = "Normal"
    elif bmi < 30:
        category = "Overweight"
    else:
        category = "Obese"
    print(f"BMI: {bmi:.1f} ({category})")
