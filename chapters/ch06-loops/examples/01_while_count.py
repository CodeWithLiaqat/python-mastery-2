# file: examples/01_while_count.py
count = 1                    # 1. shuruati value
while count <= 5:            # 2. condition
    print(f"Iteration {count}")
    count += 1               # 3. update: is ke baghair loop kabhi khatam nahi hoga
print("Loop khatam, count ab:", count)
