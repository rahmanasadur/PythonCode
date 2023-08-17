''''Exercise 6: Count the total number of digits in a number
Write a program to count the total number of digits in a number using a while loop.
For example, the number is 75869, so the output should be 5.'''

num = 75869
count = 0
while num>0:
    digit = num%10
    count = count + 1
    num = num//10
print(count)


print()
num = 123
sum = 0
while num>0:
    digit = num%10
    sum = sum + digit
    num = num//10
print(sum)


