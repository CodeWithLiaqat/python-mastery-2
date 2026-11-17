# file: examples/10_validation.py
raw = input("Umar likhein: ").strip()

if not raw:
    print("Kuch to likhein!")
elif not raw.isdigit():
    print(f"'{raw}' number nahi hai.")
else:
    age = int(raw)
    if not 1 <= age <= 120:
        print("Umar 1 se 120 ke beech honi chahiye.")
    else:
        print(f"Shukriya! Aap ki umar {age} saal hai.")
