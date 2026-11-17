# file: examples/08_input.py
# User se maloomat lena
name = input("Aap ka naam kya hai? ")
age_text = input("Aap ki umar kitni hai? ")

print("Khush aamdeed,", name)
print("age_text ki type:", type(age_text))

age = int(age_text)          # hisaab se pehle conversion zaroori
print("Agle saal aap", age + 1, "saal ke ho jayenge.")
