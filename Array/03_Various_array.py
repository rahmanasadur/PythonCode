import numpy as np
# Full Array
a = np.full((2, 2,3), 5)
b = np.full((2,3),10) 
c = np.full((2),20)
print(a)
print(b)
print(c)


# Zero array
a = np.zeros(2)
b = np.zeros((2,3))
c = np.zeros((2,3,4))

print(a)
print(b)
print(c)



# one array
# create an array filled with ones using np.ones()
array3 = np.ones((2, 4))
print("\nnp.ones():\n", array3)


# Arange array
x = np.arange(1,10,3)
print(x)



import pandas as pd
df = pd.DataFrame({"A":[1,2,3],"B":[4,5,6]})
# Add a new column
df["C"]=[7,8,9]

df["D"] = [3,4,5]
print(df)


df2 = df.mean(axis=0)
print(df2)
print(df['A'].mean())
print(np.mean(df["A"]))

print(df["A"].std())

print(df.describe())


print("###############################################")
# sort an array
a=np.array([3,5,7,1,8,2])
# Sort ascending order
s = np.sort(a)  
print(s)
# sort descending order
des = np.sort(s)[::-1]
print(des)


# Create a new random column in dataframe
df['ram'] = np.random.randint(2,5, size=len(df))
df['ram1'] = np.random.randint(2,5, size=len(df))


df.drop(['ram1'],axis=1,inplace=True)
print(df)


# Read txt file in pandas
df1 = pd.read_fwf("/home/dell/Desktop/data/Pandasdata/age.txt",delimiter='\t')
print(df1)


# read txt file in python with read
fvar = open('/home/dell/Desktop/data/txtdata/d1.txt','r')
res = fvar.read()
fvar.close()
print(res)

# read txt file in python with readline( read only first line)
fvar = open('/home/dell/Desktop/data/txtdata/d1.txt','r')
res = fvar.readline()
fvar.close()
print(res)


# read txt file in python with readlines( read only line by line.)
fvar = open('/home/dell/Desktop/data/txtdata/d1.txt','r')
res = fvar.readlines()
fvar.close()
print(res)




# create a file as string
info = """
lets all do practice
python isgood for coding
python is simple
Good morning all
Have a good day
"""

fvar =open('/home/dell/Desktop/data/txtdata/d2.txt','w')

fvar.write(info)
fvar.close()