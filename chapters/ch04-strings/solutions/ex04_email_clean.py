# file: solutions/ex04_email_clean.py
raw = "   ALI@Example.COM  "
email = raw.strip().lower()
print(email)
print("@ hai?", "@" in email)
print(".com par khatam?", email.endswith(".com"))
