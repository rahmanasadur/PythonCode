list1 = [100, 200, 300, 400, 500]
rev = []
l = len(list1)
for i in range(l-1,-1,-1):
    rev.append(list1[i])
print(rev)