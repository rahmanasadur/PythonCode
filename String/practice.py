str1 = 'I am 25 years and 10 months old'

l = str1.split()
print(l)
el = []
for item in l:
    if item.isdigit():
        el.append(item)
print(el)

l=el[0]

for j in el:
    if j>l:
        l=j
print(l)