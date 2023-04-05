#Find alpha_digit word
str1 = "Emma25 is Data scientist50 and AI Expert"

lst_str = str1.split()
anstr = []
for i in lst_str:
    if any(chr.isalpha() for chr in i) and any(chr.isdigit() for chr in i ):
        anstr.append(i)
print(anstr)

print(" ".join(anstr))


#Find max number
tpl = ('L','a','xyxa', 6, 2,3,8)
lst =list(tpl)
print(lst)
list_string = list(map(str, lst))
l3=[]
for i in list_string:
    flag=i.isalpha()
    if not flag:
        l3.append(i)

print(max(l3))

# OR
str1 = ('L','a','xyz',34,1,3,45)
large_val = 0
for i in str1:
    if(type(i).__name__ == "int"):
        if(i>=large_val):
            large_val = i

print(large_val)


# Max number from a combine alphadigti string
str2 = "Emma25 is Data scientist50 and AI Exp100ert"

lst_str = str2.split()
print(lst_str)
lst_digit = []
for i in lst_str:
    if any(chr.isalpha() for chr in i) and any(chr.isdigit() for chr in i):
        lst_digit.append(i)

print(lst_digit)

lst_digit_new = []
for i in lst_digit:
    s1=""
    for j in i:
        if j.isdigit():
            s1=s1+j
    lst_digit_new.append(s1)
print(lst_digit_new)
lst_convt_to_int = list(map(int,lst_digit_new))
print(max(lst_convt_to_int))
