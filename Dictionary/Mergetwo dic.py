dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

d3 = {**dict1,**dict2}
print(d3)

#or
d4 = dict1.copy()
d4.update(dict2)
print(d4)

#or
for i in dict2.keys():
        dict1[i]=dict2[i]
print(dict1)
