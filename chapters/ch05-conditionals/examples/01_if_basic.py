# file: examples/01_if_basic.py
temperature = 38

if temperature > 35:
    print("Bohat garmi hai!")
    print("Pani zyada piyein.")    # yeh bhi if ka hissa hai
print("Weather check mukammal.")   # yeh hamesha chalegi

order_total = 4200
if order_total >= 5000:
    print("Delivery FREE")
else:
    shortfall = 5000 - order_total
    print(f"Free delivery ke liye {shortfall} PKR ki aur shopping karein.")
