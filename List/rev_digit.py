# Write a Program to extract each digit from an integer in the reverse order.

n=7536
rv = 0
while n>0:
    digit = n%10
    n=n//10
    print(digit, end=" % ")