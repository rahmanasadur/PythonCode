# NumPy Array Slicing
# Syntax of NumPy Array Slicing
# array[start:stop:step]

# 1D NumPy Array Slicing
import numpy as np

# create a 1D array 
array1 = np.array([1, 3, 5, 7, 8, 9, 2, 4, 6])

# slice array1 from index 2 to index 6 (exclusive)
print(array1[2:6])  # [5 7 8 9]

# slice array1 from index 0 to index 8 (exclusive) with a step size of 2
print(array1[0:8:2])  # [1 5 8 2]

# slice array1 from index 3 up to the last element
print(array1[3:])  # [7 8 9 2 4 6]

# items from start to end
print(array1[:])   # [1 3 5 7 8 9 2 4 6]


print("############################################")
# Modify Array Elements Using Slicing
# 1. Using start Parameter
import numpy as np

# create a numpy array
numbers = np.array([2, 4, 6, 8, 10, 12])

# modify elements from index 3 onwards
numbers[3:] = 20
print(numbers)

# Output: [ 2  4  6 20 20 20]



print("########################################################")
# 2. Using stop Parameter
import numpy as np

# create a numpy array
numbers = np.array([2, 4, 6, 8, 10, 12])

# modify the first 3 elements
numbers[:3] = 40
print(numbers)

# Output: [40 40 40  8 10 12]


print("###############################################################")
# 3. Using start and stop parameter
import numpy as np

# create a numpy array
numbers = np.array([2, 4, 6, 8, 10, 12])

# modify elements from indices 2 to 5
numbers[2:5] = 22
print(numbers)

# Output: [2 4 22 22 22 12]


print("##############################################################")
# 4. Using start, stop, and step parameter
import numpy as np

# create a numpy array
numbers = np.array([2, 4, 6, 8, 10, 12])

# modify every second element from indices 1 to 5
numbers[1:5:2] = 16
print(numbers)

# Output: [ 2 16  6 16 10 12]


print("#################################################################")
# NumPy Array Negative Slicing
import numpy as np

# create a numpy array
numbers = np.array([2, 4, 6, 8, 10, 12])

# slice the last 3 elements of the array
# using the start parameter
print(numbers[-3:])    # [8 10 12]

# slice elements from 2nd-to-last to 4th-to-last element
# using the start and stop parameters
print(numbers[-5:-2])    # [4 6 8] 

# slice every other element of the array from the end
# using the start, stop, and step parameters
print(numbers[-1::-2])   # [12 8 4]


print("##########################################################")
# Reverse NumPy Array Using Negative Slicing
import numpy as np

# create a numpy array
numbers = np.array([2, 4, 6, 8, 10, 12])

# generate reversed array
reversed_numbers = numbers[::-1]
print(reversed_numbers)

# Output: [12 10 8 6 4 2]




print("###################################################")
# 2D NumPy Array Slicing
# create a 2D array
array1 = np.array([[1, 3, 5, 7], 
                   [9, 11, 13, 15]])

print(array1[:2, :2])

# Output

'''[[ 1  3]
 [ 9 11]]'''


print("########################################################")
# Example: 2D NumPy Array Slicing
import numpy as np

# create a 2D array 
array1 = np.array([[1, 3, 5, 7], 
                      [9, 11, 13, 15],
                      [2, 4, 6, 8]])


# slice the array to get the first two rows and columns
subarray1 = array1[:2, :2]

# slice the array to get the last two rows and columns
subarray2 = array1[1:3, 2:4]

# print the subarrays
print("First Two Rows and Columns: \n",subarray1)
print("Last two Rows and Columns: \n",subarray2)