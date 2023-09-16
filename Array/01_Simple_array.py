import numpy as np

o = np.array(4)  # o-D array
a = np.array([1,2,3,4])  # 1-D array
b = np.array([[1,2,3,4],[5,6,7,8],[1,8,5,6]])  # 2-D array
c = np.array([[[1,2,3],[4,5,6]], [[2,3,4],[5,3,4]]])   # 3-D Array

print(o)
print(a)
print(b)
print(c)

# Check dimentions
print(o.ndim)
print(a.ndim)
print(b.ndim)
print(c.ndim)

# create higher dimention array

h = np.array([[[[[1,2,3,4]]]]])
print(h)
print(h.ndim)

# or
hd = np.array([1,2,3,4], ndmin=5)
print(hd.ndim)


