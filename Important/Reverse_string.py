s="123"
revstr=" "
for i in s:
    revstr=i+revstr
print(revstr)

def my(a):
    r=a[::-1]
    return r
a="abc"
rrr=my(a)
print(rrr)

def myf(ss):
    rev=""
    for i in ss:
        rev=i+rev
    return rev
ss='1234'
r=myf('12345')
print(r)