# file: examples/09_match_patterns.py
command = "move 10 20"

match command.split():
    case ["quit"]:
        print("Band ho raha hai")
    case ["move", x, y]:
        print(f"x={x}, y={y} par ja rahe hain")
    case ["say", *words]:
        print(" ".join(words))
    case _:
        print("Command samajh nahi aayi")

temperature = 42
match temperature:
    case t if t >= 40:
        print(f"{t}°C: shadeed garmi ka alert")
    case t if t <= 0:
        print(f"{t}°C: paala")
    case t:
        print(f"{t}°C: normal")
