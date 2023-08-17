# Calculate the multiplication and sum of two numbers

n1 = int(input("Enter first no = "))
n2 = int(input("Enter 2nd no = "))
sum = n1+n2
mul = n1*n2
print("Sum = ",sum)
print("Multiplication = ", mul)


# using function

def mul_sum(n1,n2):
    sum = n1 + n2
    print(sum)
    mul= n1*n2
    print(mul)

n1 = 3
n2=4

mul_sum(n1,n2)


# or

def mul_or_sum(n1,n2):
    mul = n1*n2
    if mul<=1000:
        return mul
    else:
        return n1+n2
op = mul_or_sum(40,50)
print(op)
op = mul_or_sum(20,30)
print(op)
