age=40
get_marritial_status = lambda age : "Married" if age>30 else "Unmarried" 
print(get_marritial_status(24))

a=10
b=5
c=20
x=lambda a,b,c:a if (a>b and a>c) else b if b>c else c

print(x(a,b,c))
