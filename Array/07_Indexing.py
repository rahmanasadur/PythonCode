# Numpy Array Indexing
# Access Array Elements Using Index

import numpy as np

array1 = np.array([1, 3, 5, 7, 9])

# access numpy elements using index
print(array1[0])    # prints 1
print(array1[2])    # prints 5
print(array1[4])    # prints 9

print("########################################")
# Modify Array Elements Using Index
import numpy as np

# create a numpy array
numbers = np.array([2, 4, 6, 8, 10])

# change the value of the first element
numbers[0] = 12
print("After modifying first element:",numbers)    # prints [12 4 6 8 10]

# change the value of the third element
numbers[2] = 14
print("After modifying third element:",numbers)    # prints [12 4 14 8 10]


print("###########################################################")
# NumPy Negative Array Indexing
import numpy as np

# create a numpy array
numbers = np.array([1, 3, 5, 7, 9])

# access the last element
print(numbers[-1])    # prints 9

# access the second-to-last element
print(numbers[-2])    # prints 7


print("###################################################")
# Modify Array Elements Using Negative Indexing
import numpy as np

# create a numpy array
numbers = np.array([2, 3, 5, 7, 11])

# modify the last element
numbers[-1] = 13
print(numbers)    # Output: [2 3 5 7 13]

# modify the second-to-last element
numbers[-2] = 17
print(numbers)    # Output: [2 3 5 17 13]


print("####################################################")
# 2-D NumPy Array Indexing
import numpy as np

# create a 2D array 
array1 = np.array([[1, 3, 5, 7], 
                       [9, 11, 13, 15],
                       [2, 4, 6, 8]])


# access the element at the second row and fourth column
element1 = array1[1, 3]  # returns 15
print("4th Element at 2nd Row:",element1)  

# access the element at the first row and second column
element2 = array1[0, 1]  # returns 3
print("2nd Element at First Row:",element2)  


print("###################################################")
# Access Row or Column of 2D Array Using Indexing
import numpy as np

# create a 2D array 
array1 = np.array([[1, 3, 5], 
             [7, 9, 2], 
             [4, 6, 8]])

# access the second row of the array
second_row = array1[1, :]
print("Second Row:", second_row)  # Output: [7 9 2]

# access the third column of the array
third_col = array1[:, 2]
print("Third Column:", third_col)  # Output: [5 2 8]


print("##################################################")
# 3-D NumPy Array Indexing

import numpy as np

# create a 3D array with shape (2, 3, 4)
array1 = np.array([[[1, 2, 3, 4], 
                   [5, 6, 7, 8], 
                   [9, 10, 11, 12]],
                     
                    [[13, 14, 15, 16], 
                    [17, 18, 19, 20], 
                    [21, 22, 23, 24]]])

# access a specific element of the array
element = array1[1, 2, 1]

# print the value of the element
print(element) 
 
# Output: 22