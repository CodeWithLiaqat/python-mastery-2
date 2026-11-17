# file: examples/10_patterns.py
sales = [1200, 4500, 800, 4500, 3100, 650, 2900]

# 1. Counter: kitne items shart poori karte hain
big_sales = 0
for s in sales:
    if s > 3000:
        big_sales += 1
print("3000 se bari sales:", big_sales)

# 2. Accumulator: majmua jama karna
total = 0
for s in sales:
    total += s
print("Total:", total)

# 3. Max/Min tracking
highest = sales[0]
for s in sales:
    if s > highest:
        highest = s
print("Sab se bari:", highest)

# 4. Search: pehla match dhoondna
first_small = None
for s in sales:
    if s < 1000:
        first_small = s
        break
print("Pehli 1000 se kam sale:", first_small)

# 5. Flag: koi shart kabhi poori hui ya nahi
has_zero = False
for s in sales:
    if s == 0:
        has_zero = True
        break
print("Koi zero sale?", has_zero)
