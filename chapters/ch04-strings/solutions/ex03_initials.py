# file: solutions/ex03_initials.py
name = input("Poora naam: ")
words = name.split()
initials = ".".join(w[0].upper() for w in words) + "."
print(initials)
