# NumPy Statistical Functions
# Example 1: Compute Median for Odd Number of Elements
import numpy as np

# create a 1D array with 5 elements
array1 = np.array([1, 2, 3, 4, 5])
                                                                                                           
# calculate the median
median = np.median(array1)

print(median) 


print("##################################")
# Example 2: Compute Median for Even Number of Elements
import numpy as np

# create a 1D array with 6 elements
array1 = np.array([1, 2, 3, 4, 5, 7])

# calculate the median
median = np.median(array1)
print(median) 


print("#############################################")
#Median of NumPy 2D Array
import numpy as np

# create a 2D array
array1 = np.array([[2, 4, 6], 
                   [8, 10, 12], 
                   [14, 16, 18]])

# compute median along horizontal axis 
result1 = np.median(array1, axis=1)

print("Median along horizontal axis :", result1)

# compute median along vertical axis
result2 = np.median(array1, axis=0)

print("Median along vertical axis:", result2)

# compute median of entire array
result3 = np.median(array1)

print("Median of entire array:", result3)


print("#####################################")
# Compute Mean Using NumPy
import numpy as np

# create a numpy array
marks = np.array([76, 78, 81, 66, 85])

# compute the mean of marks
mean_marks = np.mean(marks)

print(mean_marks)


print('########################################')
# Example 3: Mean of NumPy N-d Array
import numpy as np

# create a 2D array
array1 = np.array([[1, 3], 
                 [5, 7]])

# calculate the mean of the entire array
result1 = np.mean(array1)
print("Entire Array:",result1)  # 4.0

# calculate the mean along vertical axis (axis=0)
result2 = np.mean(array1, axis=0)
print("Along Vertical Axis:",result2)  # [3. 5.]

# calculate the mean along  (axis=1)
result3 = np.mean(array1, axis=1)
print("Along Horizontal Axis :",result3)  # [2. 6.]



print("########################################")
# Example: Compute the Standard Deviation in NumPy
import numpy as np

# create a numpy array
marks = np.array([76, 78, 81, 66, 85])

# compute the standard deviation of marks
std_marks = np.std(marks)
print(std_marks)

# Output: 6.803568381206575


print("##########################################")
# Example: Compute the Standard Deviation of a 2D array.

import numpy as np

# create a 2D array
array1 = np.array([[2, 5, 9], 
                 [3, 8, 11], 
                 [4, 6, 7]])

# compute standard deviation along horizontal axis
result1 = np.std(array1, axis=1)
print("Standard deviation along horizontal axis:", result1)

# compute standard deviation along vertical axis
result2 = np.std(array1, axis=0)
print("Standard deviation  along vertical axis:", result2)

# compute standard deviation of entire array
result3 = np.std(array1)
print("Standard deviation of entire array:", result3)


print("##########################################")
# Compute Percentile of NumPy Array
import numpy as np

# create an array
array1 = np.array([1, 3, 5, 7, 9, 11, 13, 15, 17, 19])

# compute the 25th percentile of the array
result1 = np.percentile(array1, 25)
print("25th percentile:",result1)

# compute the 75th percentile of the array
result2 = np.percentile(array1, 75)
print("75th percentile:",result2)


print("###############################################")
# Find Minimum and Maximum Value of NumPy Array
import numpy as np

# create an array
array1 = np.array([2,6,9,15,17,22,65,1,62])

# find the minimum value of the array
min_val = np.min(array1)

# find the maximum value of the array
max_val = np.max(array1)

# print the results
print("Minimum value:", min_val)
print("Maximum value:", max_val)


