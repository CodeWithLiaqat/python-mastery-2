# file: solutions/ex10_sales_analysis.py
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
revenue = [120, 95, 150, 170, 80, 160]

for i, (month, rev) in enumerate(zip(months, revenue), start=1):
    print(f"{i}. {month}: {rev}k")

best = max(zip(revenue, months))
worst = min(zip(revenue, months))
print(f"Best: {best[1]} ({best[0]}k), Worst: {worst[1]} ({worst[0]}k)")

growth_months = 0
for prev, curr in zip(revenue, revenue[1:]):
    if curr > prev:
        growth_months += 1
print("Growth wale mahine:", growth_months)
