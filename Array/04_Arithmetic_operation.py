#NumPy Array Element-Wise Addition
import numpy as np

first_array = np.array([1, 3, 5, 7])
second_array = np.array([2, 4, 6, 8])

# using the + operator
result1 = first_array + second_array
print("Using the + operator:",result1) 

# using the add() function
result2 = np.add(first_array, second_array)
print("Using the add() function:",result2)


a = np.array([[1,2,3],[4,5,6]])
b = np.array([[1,2,3],[4,5,6]])
result = a+b
print(result)
# By add function
result = np.add(a,b)
print(result)

a = np.array([[[1,2,],[3,4]],[[5,6],[7,8]]])
b = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
result = a+b
print(result)
print(np.add(a,b))

print("###################################")

# NumPy Array Element-Wise Subtraction

import numpy as np

first_array = np.array([3, 9, 27, 81])
second_array = np.array([2, 4, 8, 16])

# using the - operator
result1 = first_array - second_array
print("Using the - operator:",result1) 

# using the subtract() function
result2 = np.subtract(first_array, second_array)
print("Using the subtract() function:",result2) 


print("#########################################")
#NumPy Array Element-Wise Multiplication

import numpy as np

first_array = np.array([1, 3, 5, 7])
second_array = np.array([2, 4, 6, 8])

# using the * operator
result1 = first_array * second_array
print("Using the * operator:",result1) 

# using the multiply() function
result2 = np.multiply(first_array, second_array)
print("Using the multiply() function:",result2) 


print("############################################")
#NumPy Array Element-Wise Division
import numpy as np

first_array = np.array([1, 2, 3])
second_array = np.array([4, 5, 6])

# using the / operator
result1 = first_array / second_array
print("Using the / operator:",result1) 

# using the divide() function
result2 = np.divide(first_array, second_array)
print("Using the divide() function:",result2) 


print("#######################################")
# NumPy Array Element-Wise Exponentiation
import numpy as np

array1 = np.array([1, 2, 3])

# using the ** operator
result1 = array1 ** 2
print("Using the ** operator:",result1) 

# using the power() function
result2 = np.power(array1, 2)
print("Using the power() function:",result2) 
print(np.power(array1,3))


print("################################################")
# NumPy Array Element-Wise Modulus
import numpy as np

first_array = np.array([9, 10, 20])
second_array = np.array([2, 5, 7])

# using the % operator
result1 = first_array % second_array
print("Using the % operator:",result1) 

# using the mod() function
result2 = np.mod(first_array, second_array)
print("Using the mod() function:",result2)