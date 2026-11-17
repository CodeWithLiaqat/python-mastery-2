# file: examples/07_membership.py
email = "sana@example.com"
print("@" in email)
print(" " not in email)

big_cities = ("Karachi", "Lahore", "Faisalabad")
city = "Lahore"
print(city in big_cities)
print("lahore" in big_cities)     # case-sensitive
