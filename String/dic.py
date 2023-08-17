# Write a program to count occurrences of all characters within a string


str1 = "Apple"
char_dic = {}
count =0
for i in str1:
    count = str1.count(i)
    char_dic[i]=count
print(char_dic)