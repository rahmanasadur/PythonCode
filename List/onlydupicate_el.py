
# program to print duplicate numbers in a given list
lst = [0,1,2,3,1,3,2,4,5,2,3,2,7,7]
dup_list = []
for i in lst:
    count = lst.count(i)
    if count>1:
        if dup_list.count(i)==0:
            dup_list.append(i)
print(dup_list)

# method 2
lst2 = [1,2,2,3,3,4,5,6,6]
uni_list = []
dup_list = []
for i in lst2:
    cnt = lst2.count(i)
    if cnt>1:
        if dup_list.count(i)==0:
            dup_list.append(i)
    else:
        uni_list.append(i)

print(dup_list)
print(uni_list)