# file: examples/04_nested_atm.py
CORRECT_PIN = "1234"
balance = 25_000

pin = input("PIN: ")
if pin == CORRECT_PIN:
    amount = int(input("Kitni raqam? "))
    if amount <= balance:
        if amount % 500 == 0:
            balance -= amount
            print(f"{amount} nikal liye. Baqi: {balance}")
        else:
            print("Raqam 500 ke multiple mein honi chahiye.")
    else:
        print("Balance kaafi nahi.")
else:
    print("Ghalat PIN.")
