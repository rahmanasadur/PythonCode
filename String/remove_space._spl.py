# Remove empty strings from a list of strings


str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
after_remove = []
for i in str_list:
    if i:
        after_remove.append(i)
print(after_remove)



#------------------------------------------------
import re 
# With re
str1 = "/*Jon is @developer & musician"
s = re.sub('[*/@&]',"",str1)
print(s)

print()

#2nd method without re
print(str1.replace("&","").replace("*",'').replace("/",'').replace("@",''))