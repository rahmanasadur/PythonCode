from functools import reduce

InputList = input("Enter Numbers:").split()
print(InputList)

def add(*agrs):
    newlist = []
    for i in InputList:
        z = int(i)
        newlist.append(z)
    result = sum(newlist)
    return result


def sub(*agrs):
    newlist = []
    for i in InputList:
        z = int(i)
        newlist.append(z)
    result = newlist[0]-sum(newlist[1:])
    return result

def mul(*agrs):
    newlist = []
    for i in InputList:
        z = int(i)
        newlist.append(z)
    result = reduce(lambda x,y:x*y,newlist)
    return result

def div(*agrs):
    newlist = []
    for i in InputList:
        z = int(i)
        newlist.append(z)
    result = reduce(lambda x,y: x/y,newlist)
    return result

print("Enter Operator:\n"
        "1-> Add\n"
        "2-> Sub\n"
        "3-> Mul\n"
        "4-> Div\n")
choice = int(input("Enter your choice: "))

if choice == 1:
    result = add(InputList)
    print(result)
elif choice == 2:
    result = sub(InputList)
    print(result)
elif choice == 3:
    result = mul(InputList)
    print(result)
elif choice == 4:
    result = div(InputList)
    print(result)
    
else:
    print("Invalid Choice")
