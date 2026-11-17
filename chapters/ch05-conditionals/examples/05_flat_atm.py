# file: examples/05_flat_atm.py
CORRECT_PIN = "1234"
balance = 25_000

pin = input("PIN: ")
amount = int(input("Kitni raqam? ")) if pin == CORRECT_PIN else 0

if pin != CORRECT_PIN:
    print("Ghalat PIN.")
elif amount > balance:
    print("Balance kaafi nahi.")
elif amount % 500 != 0:
    print("Raqam 500 ke multiple mein honi chahiye.")
else:
    balance -= amount
    print(f"{amount} nikal liye. Baqi: {balance}")
