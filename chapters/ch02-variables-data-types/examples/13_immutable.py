# file: examples/13_immutable.py
score = 50
old_id = id(score)

score = score + 10
print("Nayi value:", score)
print("Kya wahi object hai?", id(score) == old_id)

city = "lahore"
city.upper()                 # naya string banata hai, city ko nahi badalta
print("city abhi bhi:", city)
city = city.upper()          # natija wapas usi naam ko assign kiya
print("city ab:", city)
