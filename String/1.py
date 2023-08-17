s = "asadur"
print(s[0:])
print(s[0::2])  # Increment by 2
print(s[::-1])  # reverse
print(s[::-2])  # revere decrement by 2
print(s[:-1:-1])

l = len(s)

for i in range(0,l-1,2):
    print(s[i])


x=list(s)
for i in (x[0::2]):
    print(i)


# Display numbers divisible by 5 from a list

lst = [10, 20, 33, 46, 55]

emp_list = []
for i in lst:
    if i%5==0:
        emp_list.append(i)
print(emp_list)

#or

for i in lst:
    if i%5==0:
        print(i)