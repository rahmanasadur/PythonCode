# Removal all characters from a string except integers

str1 = 'I am 25 years and 10 months old'

l = str1.split()
el = []
for item in l:
    if item.isdigit():
        el.append(item)
print("".join(el))


# Find words with both alphabets and numbers

str1 = "Emma25 is Data scientist50 and AI Expert"
l = str1.split()
print(l)
el = []
for item in l:
    if any(char.isalpha() for char in item) and any(char.isdigit() for char in item):
        el.append(item)
print(el)
for i in el:
    print(i)


# Find words with both alphabets and numbers


str1 = "Emma25 is Data scientist50 and AI Expert"
l = str1.split()
print(l)
el = []
for item in l:
    if any(char.isalpha() for char in item) and any(char.isdigit() for char in item):
        el.append(item)
print(el)


# Find the lagest num.

s2 = "Emma 25 is Data scientist 50 and 10 AI Expert"
l2 = s2.split()
el2 = []
for item in l2:
    if item.isdigit():
        el2.append(item)
print(el2)

max = el2[0]

for j in el2:
    if j>max:
        max=j

print(max)