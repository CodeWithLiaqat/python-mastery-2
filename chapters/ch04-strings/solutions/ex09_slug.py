# file: solutions/ex09_slug.py
title = "  Python Seekhein: Zero Se Hero!  "
cleaned = title.strip().lower().replace(":", "").replace("!", "")
slug = "-".join(cleaned.split())
print(slug)
