# file: examples/07_methods_case.py
raw = "   pAKistan zINDABAD   "
print(f"[{raw.strip()}]")          # dono taraf ke spaces hatao
print(f"[{raw.lstrip()}]")         # sirf baayein
print(f"[{raw.rstrip()}]")         # sirf daayein
clean = raw.strip()
print(clean.upper())
print(clean.lower())
print(clean.title())               # har lafz ka pehla harf capital
print(clean.capitalize())          # sirf pehla harf capital
print(clean.swapcase())
