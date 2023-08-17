# Calculate the sum of all numbers from 1 to a given number

n = int(input("enter a number:"))
i=1
sum=0
while i<=n:
    sum = sum + i
    i = i+1
print(sum)

#or 
sum1 = 0
for i in range(1,n+1):
    sum1 = sum1 + i
print(sum1)
