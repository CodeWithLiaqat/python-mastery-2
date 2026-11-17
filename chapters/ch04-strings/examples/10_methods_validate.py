# file: examples/10_methods_validate.py
print("12345".isdigit())
print("12.5".isdigit())        # point digit nahi
print("Ali".isalpha())
print("Ali Khan".isalpha())    # space alpha nahi
print("Room101".isalnum())
print("   ".isspace())
print("LAHORE".isupper(), "lahore".islower())
