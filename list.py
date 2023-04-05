n = int(input())
m = input()
m = m.split(" ")
t = []
for i in m:
    j = int(i)

    t.append(j)
t = tuple(t)
h = hash(t)
print(h)