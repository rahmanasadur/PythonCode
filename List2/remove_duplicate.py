# Remove duplicate

list1 = [5, 20, 15, 20, 25, 50, 20]

dup = []
for i in list1:
    if i not in dup:
        dup.append(i)
print(dup)