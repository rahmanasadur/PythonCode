n=123
rev=0
sum=0

while n>0:
    digit=n%10
    rev=rev*10+digit
    sum=sum+digit
    n=int(n/10)
result = (rev/sum).as_integer_ratio()
print(str(result[0])+":"+str(result[1]))
print(rev)
print(sum)


