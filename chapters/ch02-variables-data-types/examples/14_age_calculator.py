# file: examples/14_age_calculator.py
# Age Calculator
CURRENT_YEAR = 2026

name = input("Naam: ")
birth_year = int(input("Paidaish ka saal: "))

age = CURRENT_YEAR - birth_year
year_of_100 = birth_year + 100

print("-" * 35)
print(f"{name}, {CURRENT_YEAR} mein aap ki umar {age} saal hai.")
print(f"Aap {year_of_100} mein 100 saal ke honge.")
print(f"Yaani abhi {year_of_100 - CURRENT_YEAR} saal baqi hain.")
