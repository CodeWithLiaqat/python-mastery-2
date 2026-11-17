# file: examples/06_conversion.py
# Implicit conversion
total = 10 + 2.5
print(total, type(total))

# Explicit conversion
print(int("42") + 8)        # text -> int
print(float("99.99"))       # text -> float
print(int(9.99))            # float -> int: decimal KAT jata hai, round nahi hota
print(round(9.99))          # round karna ho to round()
print(str(2025) + " mein")  # int -> text, taake text ke saath jor sakein
print(float(7))             # int -> float

# bool() conversion: "khaali" cheezein False hain
print(bool(0), bool(0.0), bool(""), bool(None))
print(bool(5), bool(-1), bool("0"), bool(" "))
