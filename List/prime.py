# Check a num is prime or not

n=3
if n>1:
    for i in range(2,n):
        if n%i==0:
            print("not prime")
            break
    else:
        print("prime")


#2. range of ime num

for num in range(25,51):
    if num>2:
        for i in range(2,num):
            if num%i==0:
                break

        else:
            print(num)



#3. generate a list only rrime num from a given list
l = [3,4,5,6,7,8,9]
prime_list = []
for num in l:
    if num>2:
        for i in range(2,num):
            if num%i==0:
                break

        else:
            prime_list.append(num)

print(prime_list)
