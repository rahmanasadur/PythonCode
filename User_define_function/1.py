# A function is a block of code we can used again and again

# 1. simple function
def simple():
    print("wel come")
simple()

# 2. function th argument
def sum(a,b):
    print(a+b)

a=10
b=20
sum(a,b)


# 3. return type
def add(a,b):
    c = a+b
    return c

op = add(10,30)
print(op)
