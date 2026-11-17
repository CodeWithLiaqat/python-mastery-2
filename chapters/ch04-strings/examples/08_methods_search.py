# file: examples/08_methods_search.py
sentence = "Python seekhna asaan hai aur Python mazedaar hai"
print(sentence.find("Python"))        # pehla index
print(sentence.find("Java"))          # na mile to -1
print(sentence.rfind("Python"))       # aakhri occurrence
print(sentence.count("hai"))
print(sentence.startswith("Python"))
print(sentence.endswith("hai"))
print("Python" in sentence)
