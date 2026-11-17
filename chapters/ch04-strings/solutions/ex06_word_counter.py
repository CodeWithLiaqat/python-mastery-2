# file: solutions/ex06_word_counter.py
sentence = "Python asaan hai aur Python ki community bari hai"
words = sentence.split()
print("Alfaaz:", len(words))
print("Characters (spaces ke baghair):", len(sentence.replace(" ", "")))
print("'hai' ki ginti:", words.count("hai"))
