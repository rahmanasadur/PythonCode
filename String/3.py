# Create a string made of the first, middle and last character

str1 = "James"
first_char = str1[0]
last_char = str1[-1]
l = len(str1)
mid = int(l/2)
mid_char = str1[mid]

res = first_char+mid_char+last_char
print(res)


print()

#Create a string made of the middle three characters

str1 = "JhonDipPeta"
l = len(str1)
mid = int(l/2)

middle = str1[mid]
left_mid = str1[mid-1]
right_mid = str1[mid+1]
res = left_mid+middle+right_mid
print(res)


# Append new string in the middle of a given string
s1 = "Ault"
s2 = "Kelly"

ss1 = [*s1]
print(ss1)
ss2 = [*s2]
ss1.insert(2,s2)
s = "".join(ss1)
print(s)
