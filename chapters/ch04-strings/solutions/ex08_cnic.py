# file: solutions/ex08_cnic.py
cnic = input("CNIC: ").strip()
digits = cnic.replace("-", "")
is_valid = (len(cnic) == 15 and cnic[5] == "-" and cnic[13] == "-"
            and digits.isdigit() and len(digits) == 13)
print("Valid:", is_valid)
print("Province code:", cnic[0])
