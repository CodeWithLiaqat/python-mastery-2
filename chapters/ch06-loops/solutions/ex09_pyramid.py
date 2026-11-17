# file: solutions/ex09_pyramid.py
height = int(input("Height: "))
for row in range(1, height + 1):
    spaces = height - row
    stars = 2 * row - 1
    print(" " * spaces + "*" * stars)
