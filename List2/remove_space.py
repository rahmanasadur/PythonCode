# Remove empty strings from the list of strings


list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]

l = []
for i in list1:
    if i:
        l.append(i)
print(l)


# or 
l1=list(filter(None,list1))
print(l1)