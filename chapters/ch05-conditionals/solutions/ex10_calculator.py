# file: solutions/ex10_calculator.py
expression = input("Expression (e.g. 12 * 4): ")

match expression.split():
    case [a, "+", b]:
        print(float(a) + float(b))
    case [a, "-", b]:
        print(float(a) - float(b))
    case [a, "*", b]:
        print(float(a) * float(b))
    case [a, "/", b]:
        if float(b) == 0:
            print("Zero se taqseem mumkin nahi.")
        else:
            print(float(a) / float(b))
    case [_, op, _]:
        print(f"'{op}' operator support nahi hota.")
    case _:
        print("Format: number operator number (spaces ke saath)")
