#Q1
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
# op = {'Ten': 30, 'Twenty': 30, 'Thirty': 30}

d = {}
for i in keys:
    for j in values:
        d[i]=j
print(d)

#or

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
# op = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
d1 = {}
d1 = dict(zip(keys,values))
print(d1)

# or by loop and update method

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
d2 = {}
l = len(keys)
for i in range(l):
    d2.update({keys[i]:values[i]})
print(d2)