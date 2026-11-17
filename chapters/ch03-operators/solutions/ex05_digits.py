# file: solutions/ex05_digits.py
n = int(input("3-digit number: "))
hundreds = n // 100
tens = (n // 10) % 10
ones = n % 10
print(f"Digits: {hundreds}, {tens}, {ones}")
print(f"Majmua: {hundreds + tens + ones}")
