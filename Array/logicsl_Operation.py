# Example 1: NumPy Comparison Operators
import numpy as np

array1 = np.array([1, 2, 3])
array2 = np.array([3, 2, 1])

# less than operator
result1 = array1 < array2
print("array1 < array2:",result1)    # Output: [ True False False]

# greater than operator
result2 = array1 > array2
print("array1 > array2:",result2)    # Output: [False False  True]

# equal to operator
result3 = array1 == array2
print("array1 == array2:",result3)    # Output: [False  True False]

print("#############################################")
# NumPy Comparison Functions
import numpy as np

array1 = np.array([9, 12, 21])
array2 = np.array([21, 12, 9])

# use of less()
result = np.less(array1, array2)
print("Using less():",result)    # Output: [ True False False]

# use of less_equal()
result = np.less_equal(array1, array2)
print("Using less_equal():",result)     # Output: [ True  True False]

# use of greater()
result = np.greater(array1, array2)
print("Using greater():",result)    # Output: [False False  True]

# use of greater_equal()
result = np.greater_equal(array1, array2)
print("Using greater_equal():",result)    # Output: [False  True  True]

# use of equal()
result = np.equal(array1, array2)
print("Using equal():",result)    # Output: [False  True False]

# use of not_equal()
result = np.not_equal(array1, array2)
print("Using not_equal():",result)    # Output: [ True False  True]


print("################################################")
# Example 3: NumPy Logical Operations
import numpy as np

x1 = np.array([True, False, True])
x2 = np.array([False, False, True])

# Logical AND
print(np.logical_and(x1, x2)) # Output: [False False  True]

# Logical OR
print(np.logical_or(x1, x2)) # Output: [ True False  True]

# Logical NOT
print(np.logical_not(x1)) # Output: [False  True False]