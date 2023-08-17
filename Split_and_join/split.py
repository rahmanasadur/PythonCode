s = "asadur"
print(*s)

print()

print([*s])

print()
l=[]
for i in s:
    l.append(i)
print(l)


s1 = "asadur#Rahman"
s2 = s1.split("#")
print(s2)


# Join
j = " ".join(s2)
print(j)


print()
# sub split
str1 = "Emma-is-a-data-scientist"

sub_str = str1.split("-")
for i in sub_str:
    print(i)

