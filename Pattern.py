print("1-----------------------------")
l=4
for i in range(1,l):
    print("* "*i,end=" ")
    print("\n")
for i in range(l,0,-1):
    if i==2:
        continue
    print("* "*i,end=" ")
    print("\n")

print("2-------------------------")
l=4
for i in range(0,l):
    print("* "*l,end=" ")
    print("\n")

print("3-------------------------")
rows_no=4
for i in range (rows_no, 0, -1):
    print(" "*(rows_no-i) +"* "*i, end='')
    print("\n")


print("4-----------------------")
l=4
for i in range(0,l):
    print("* "*i,end=" ")
    print("\n")

print("5-------------------------")
l=4
for i in range(l,0,-1):
    print("* "*i,end=" ")
    print("\n")

print("6-------------------------")
l=4
for i in range(l,0,-1):
    print("* "*l,end=" ")
    print("\n")

print("7-------------------------")
l=4
for i in range(l,0,-1):
    print(""*(l-i)+"* "*i,end=" ")
    print("\n")

print("8-------------------------")
l=4
for i in range(l,0,-1):
    print(" "*(l-i)+"* "*i,end=" ")
    print("\n")

print("9-------------------------")
l=4
for i in range(l,0,-1):
    print("  "*(l-i)+"* "*i,end=" ")
    print("\n")

print("10-------------------------")
l=5
for i in range(0,l):
    print("  "*(l-i)+"* "*i,end=" ")
    print("\n")

print("11-------------------------")
l=5
for i in range(0,l):
    print(" "*(l-i)+"* "*i,end=" ")
    print("\n")

print("12-------------------------")
l=5
for i in range(0,l):
    print(""*(l-i)+"* "*i,end=" ")
    print("\n")
    