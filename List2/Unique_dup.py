l = [1,2,3,3,4,4,5,5]
dup = []
u = []
for i in l:
    cnt = l.count(i)
    if cnt>1:
        if dup.count(i)==0:
            dup.append(i)
    else:
        u.append(i)


print(dup)
print(u)