# file: solutions/ex06_eligibility.py
age = int(input("Umar: "))
marks = int(input("Marks: "))
sports_quota = input("Sports quota? (True/False): ") == "True"

eligible = (16 <= age <= 25) and (marks >= 80 or sports_quota)
print("Eligible:", eligible)
