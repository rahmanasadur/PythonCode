# Write a program to print multiplication table of a given number

n =int(input("enter an no:"))
for i in range(1,11):
    print(i,"x",n, "=", i*n)

print()


for i in range(10,0,-1):
    print(i,"x",n, "=", i*n)