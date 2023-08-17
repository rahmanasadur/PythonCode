# Create a new list from a two list using the following condition

list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]
odd_list = []
even_list = []
for i in list1:
    if i%2!=0:
        odd_list.append(i)
for j in list2:
    if j%2==0:
        even_list.append(j)
odd_list.extend(even_list)
print(odd_list)
