# Reverse a string

s = "abcd"
#print(s[::-1])
rev_str = ""
for i in s:
    rev_str = i+rev_str
print(rev_str)


s1 = "1234"
rev_str = ""
l = len(s1)
for i in range(l-1,-1,-1):
    rev_str = rev_str + s1[i]
print(rev_str)