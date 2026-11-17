# file: examples/06_loop_else.py
roll_numbers = [101, 104, 108, 112]
target = 109

for roll in roll_numbers:
    if roll == target:
        print(f"Roll {target} mil gaya!")
        break
else:
    print(f"Roll {target} list mein nahi hai.")
