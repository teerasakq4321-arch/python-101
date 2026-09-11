cols = int(input("How many colums :"))
rows = int(input("How many rows :"))

num = 1
for r in range(rows):
    for c in range(cols):
        print(f"{num:4d}",end="")
        num += 1
    print()
