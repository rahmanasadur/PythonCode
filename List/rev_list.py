# Print list in reverse order using a loop


list1 = [10, 20, 30, 40, 50]
print(list1[::-1])
list1.sort(reverse=True)
print(list1)

print()

#0r
list2 = [10, 20, 30, 40, 50]
l = len(list2)
for i in range(l-1,-1,-1):
    print(list2[i])


print()

#or
list3 = [10, 20, 30, 40, 50]
rev_list = []
l = len(list3)
for i in range(l-1,-1,-1):
    rev_list.append(list3[i])

print(rev_list)