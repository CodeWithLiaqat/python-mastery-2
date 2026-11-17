# file: examples/09_methods_split_join.py
phone = "0300-123-4567"
print(phone.replace("-", ""))
print(phone.replace("-", " ", 1))     # sirf pehli dafa

csv_line = "Ali,Lahore,25,Engineer"
parts = csv_line.split(",")
print(parts)
print(parts[1])

words = "  Python   is   fun  ".split()     # baghair argument: kisi bhi whitespace par
print(words)

print(" | ".join(["Karachi", "Lahore", "Quetta"]))
print("-".join("ABC"))
