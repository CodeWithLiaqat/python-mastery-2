# file: examples/05_type_id.py
# type() aur dynamic typing
value = 100
print(value, type(value))

value = "sau"
print(value, type(value))

value = 99.5
print(value, type(value))

# id(): do naam aik hi object ki taraf
a = "Pakistan"
b = a
print("a aur b aik hi object?", id(a) == id(b))
print("is se bhi check:", a is b)
