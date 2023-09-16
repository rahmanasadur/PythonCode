# it is an anonymous functions means that the function is without a name
# lambda keyword is used to defined th function
# it can take any number of arguments but only one expression
# Syntax= lambda arguments:expression

#1.
x = lambda a : a + 5
print(x(10))

#2.
x = lambda a,b,c : a + b + c
print(x(5,10,20))

print( ' ')

# find largest number 
num = lambda a,b,c: a if(a>b and a>c) else b if b>a and b>c else c
print(num(2,4,3))

# check between 10 and 20
n1 = lambda x : True if(x>10 and x<20) else False
print(n1(16))

n2 = lambda a,b : a if(a>b) else b
print(n2(2,6))


n3 = lambda a : a*2 if(a<10) else(a*3 if a>10 and a<20 else a)
print(n3(4))
print(n3(12))
print(n3(45))

n4 = lambda a : 'even' if a%2==0 else 'odd'
print(n4(3))

def myfunc(n):
    x = lambda a : a * n
    return x

mydoubler = myfunc(2)

print(mydoubler(11))