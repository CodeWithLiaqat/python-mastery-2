# file: examples/12_guessing_game.py
# Mini Project 2: Number Guessing Game
import random

random.seed(7)                 # sirf kitab ke output ko fix rakhne ke liye; asal game mein hata dein
MAX_ATTEMPTS = 7
secret = random.randint(1, 100)

print("=== NUMBER GUESSING GAME ===")
print(f"Maine 1 se 100 ke beech aik number socha hai. Aap ke paas {MAX_ATTEMPTS} koshishein hain.")

attempts = 0
while attempts < MAX_ATTEMPTS:
    guess_text = input(f"Koshish {attempts + 1}: ").strip()

    if not guess_text.isdigit() or not 1 <= int(guess_text) <= 100:
        print("  1 se 100 ke beech number likhein (yeh koshish gini nahi gayi).")
        continue

    guess = int(guess_text)
    attempts += 1

    if guess == secret:
        print(f"Mubarak ho! {attempts} koshishon mein sahi jawab: {secret}")
        break
    elif guess < secret:
        print("  Zyada socho ↑")
    else:
        print("  Kam socho ↓")
else:
    print(f"Koshishein khatam! Number tha: {secret}")
