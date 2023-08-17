# Arrange string characters such that lowercase letters should come first
str1 = 'PyNaTive'
l = ""
u = ""
for i in str1:
    if i.islower():
        l = l+i
    if i.isupper():
        u = u+i
print(l+u)


#Count all letters, digits, and special symbols from a given string

str1 = "P@#yn26at^&i5ve"

count_char = 0
count_digit = 0
count_splchar = 0
for i in str1:
    if i.isalpha():
        count_char = count_char+1
    elif i.isdigit():
        count_digit = count_digit +1
    else:
        count_splchar = count_splchar+1

print(count_char, count_digit, count_splchar)

#Calculate the sum and average of the digits present in a string

str1 = "PYnative29@#8496"
total = 0
cnt = 0
for i in str1:
    if i.isdigit():
        total = total+int(i)
        cnt = cnt+1

print("sum:",total)
print("avg:",total/cnt)
