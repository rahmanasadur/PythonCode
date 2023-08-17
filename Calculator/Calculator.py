n1 = int(input("enter 1st no:"))
n2 = int(input("Enter 2nd no:"))
op = input("enter an opr:")

if op =="1":
    c = n1+n2
elif op =="2":
    c = n1-n2
elif op =="3":
    c = n1*n2
elif op =="4":
    c = n1/n2
else:
    print("Invalid Opr")
print(c)