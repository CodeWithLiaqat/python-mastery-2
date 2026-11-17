# file: examples/08_is_vs_equal.py
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a == b)    # values barabar
print(a is b)    # do alag objects
print(a is c)    # c aur a aik hi object

result = None
print(result is None)   # None check ka sahi tareeqa
