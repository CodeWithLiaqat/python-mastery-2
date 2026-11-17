# file: examples/08_match_menu.py
print("1. Balance  2. Deposit  3. Withdraw  0. Exit")
choice = input("Option: ")

match choice:
    case "1":
        print("Aap ka balance: 25,000")
    case "2" | "3":
        action = "Deposit" if choice == "2" else "Withdraw"
        print(f"{action} screen khul rahi hai...")
    case "0":
        print("Allah Hafiz!")
    case _:
        print("Ghalat option")
