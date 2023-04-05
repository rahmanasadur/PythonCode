'''
lst = ['a', 1, 'b', 2, 'c', 3]
count=0

res_dict = {}
for i in range(0,len(lst),2):
    res_dict[lst[i]] = lst[i+1]
     
print(res_dict)
'''
'''
lst=['a','b','a','a','b','b','c','d','d','e']
dic={}
for i in lst:
    dic[i]=lst.count(i)

print(dic)
'''


lst=['a','b','a','a','b','b','c','d','d','e']

x="a"
count=0
for i in lst:
    if i=="a":
        count=count+1
print(count)

'''
#Make dic without count function
lst=['a','b','a','a','b','b','c','d','d','e']
dic={}
for i in lst:
    if i not in dic:
        dic[i]=1
    else:
      dic[i]=dic[i]+1  
print(dic)
'''

#Change key to value and value to key
dic1={"a":1,"b":2,"c":3}
swap_dic={}
for k,v in dic1.items():
    swap_dic[v]=k
print(swap_dic)


dic2 = {'A':'a','B':{'B1':1,'B2':2},'C':'c','D':{'D1':1,'D2':2,'D3':3}}

b1 = {'B1':1,'B2':2}
def modify_dic_value(b1):
    for k,v in b1.items():
        value_type = type(v).__name__
        if value_type == 'int':
            b1[k] = k
    return b1
b = modify_dic_value(b1)
print(b)

d1 = {'D1':1,'D2':2}
def modify_dic1_value(d1):
    for k,v in d1.items():
        value_type = type(v).__name__
        if value_type == 'int':
            d1[k] = k
    return d1
d = modify_dic_value(d1)
print(d)




