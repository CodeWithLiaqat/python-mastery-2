# file: solutions/ex07_phone.py
phone = input("Mobile number: ").strip()
is_valid = phone.isdigit() and len(phone) == 11 and phone.startswith("03")
print("Valid:", is_valid)
print("Formatted:", phone[:4] + "-" + phone[4:])
