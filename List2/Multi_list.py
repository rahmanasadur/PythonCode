# Add new item to list after a specified item

list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
print(list1[0])
print(list1[1])
print(list1[2])

list1[2][2].append(7000)
print(list1)

list1[2].append(7000)
print(list1)

print()

#2
list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]

# sub list to add
sub_list = ["h", "i", "j"]

# OP = ['a', 'b', ['c', ['d', 'e', ['f', 'g', 'h', 'i', 'j'], 'k'], 'l'], 'm', 'n']

print(list1[1])
print(list1[2])
print(list1[2][1])
print(list1[2][1][2])

list1[2][1][2].extend(sub_list)
print(list1)