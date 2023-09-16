# NumPy Array Manipulation Functions
import numpy as np

# create a 1D array
array1 = np.array([1, 3, 5, 7, 9, 11])

# reshape the 1D array into a 2D array
array2 = np.reshape(array1, (2, 3))

# transpose the 2D array
array3 = np.transpose(array2)

print("Original array:\n", array1)
print("\nReshaped array:\n", array2)
print("\nTransposed array:\n", array3)

# create a 1D array
a = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
# reshape the 1D array into a 3D array
b = np.reshape(a, (3, 2,2))
c = np.reshape(a, (2, 2,3))
t = np.transpose(c)
print(a)
print(b)
print(c)
print(t)


print("############################################")
# NumPy Array Statistical Functions
import numpy as np

# create a numpy array
marks = np.array([76, 78, 81, 66, 85])

# compute the mean of marks
mean_marks = np.mean(marks)
print("Mean:",mean_marks)

# compute the median of marks
median_marks = np.median(marks)
print("Median:",median_marks)

# find the minimum and maximum marks
min_marks = np.min(marks)
print("Minimum marks:", min_marks)

max_marks = np.max(marks)
print("Maximum marks:", max_marks)


import statistics as st

a = np.array([1,2,3,4, 4])
# compute the mode of marks
mode_marks = st.mode(a)
print("Mode:",mode_marks)


print("#################################")
# NumPy Array Input/Output Functions
import numpy as np

# create an array
array1 = np.array([[1, 3, 5], [2, 4, 6]])

# save the array to a text file
np.savetxt('/home/dell/Desktop/data/array/data.txt', array1)

# load the data from the text file
loaded_data = np.loadtxt('/home/dell/Desktop/data/array/data.txt')

# print the loaded data
print(loaded_data)

