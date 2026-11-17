# file: examples/02_while_validation.py
age_text = input("Umar (1-120): ")
while not (age_text.isdigit() and 1 <= int(age_text) <= 120):
    print("  Ghalat input, dobara koshish karein.")
    age_text = input("Umar (1-120): ")

age = int(age_text)
print(f"Shukriya! Umar: {age}")
