import numpy as np

# print(np.__version__)

# print(np.info(np.add))

x = np.array([1,2,4,5,8])
y = np.array([0,1,2,4,5,8])
print(x)
print(np.all(x))
print(y)
print(np.all(y))
print(np.any(x)) 
y = np.array([0,0,0,0,0])
print(np.any(y)) 

a = np.array([1, 0, np.nan, np.inf])

# Printing the original array 'a'
print("Original array")
print(a)

# Checking the given array 'a' element-wise for finiteness and printing the result
print("Test a given array element-wise for finiteness :")
print(np.isfinite(a)) 

a = np.array([1+1j, 1+0j, 4.5, 3, 2, 2j])

# Printing the original array 'a'
print("Original array")
print(a)

# Checking the given array 'a' element-wise for complex numbers and printing the result
print("Checking for complex number:",np.iscomplex(a))

# Checking the given array 'a' element-wise for real numbers and printing the result
print("Checking for real number:",np.isreal(a))
print()

# Checking if a value is a scalar or not (in this case, checking if 3.1 is a scalar)
print("Checking for scalar type:",np.isscalar(3.1))
print()

# Checking if a list ([3.1]) is a scalar or not (in this case, it's not a scalar)
print(np.isscalar([3.1])) 


x = np.array([3, 5])
y = np.array([2, 5])

# Printing the original numbers stored in arrays 'x' and 'y'
print("Original numbers:")
print(x)
print(y)

# Performing element-wise comparison (greater than) between arrays 'x' and 'y', and printing the result
print("Comparison - greater")
print(np.greater(x, y))

# Performing element-wise comparison (greater than or equal to) between arrays 'x' and 'y', and printing the result
print("Comparison - greater_equal")
print(np.greater_equal(x, y))

# Performing element-wise comparison (less than) between arrays 'x' and 'y', and printing the result
print("Comparison - less")
print(np.less(x, y))

# Performing element-wise comparison (less than or equal to) between arrays 'x' and 'y', and printing the result
print("Comparison - less_equal")
print(np.less_equal(x, y))

# Creating an array of integers from 30 to 70 using np.arange()
array_int = np.arange(30, 71)
array_even = np.arange(30, 71 , 2)
array_odd = np.arange(31, 71 , 2)

# Printing a message indicating an array of integers from 30 to 70
print("Array of the integers from 30 to 70")

# Printing the array of integers from 30 to 70
print("integers",array_int) 
print("even num",array_even)
print("odd num",array_odd)

array_2D = np.identity(3)

# Printing a message indicating a 3x3 matrix
print('3x3 matrix:')

# Printing the 3x3 identity matrix
print(array_2D) 

rand_num = np.random.normal(0, 1, 1)

# Printing a message indicating a random number between 0 and 1
print("Random number between 0 and 1:")

# Printing the generated random number
print(rand_num)

rand_num = np.random.normal(0, 1, 30)

# Printing a message indicating 15 random numbers from a standard normal distribution
print("15 random numbers from a standard normal distribution:")

# Printing the array of 15 random numbers
print(rand_num) 

a = np.arange(10, 22).reshape((3, 4))

# Printing a message indicating the original array 'a'
print("Original array:")
print(a)

# Printing a message indicating each element of the array using np.nditer() to iterate through the elements
print("Each element of the array is:")
for x in np.nditer(a):
    print(x, end=" ") 

x = np.array([1, 8, 3, 5])

# Printing a message indicating Vector-1 and displaying the array 'x'
print("Vector-1")
print(x)

# Generating a NumPy array 'y' containing 4 random integers between 0 and 10 using np.random.randint()
y = np.random.randint(0, 11, 4)

# Printing a message indicating Vector-2 and displaying the array 'y'
print("Vector-2")
print(y)

# Performing element-wise multiplication between arrays 'x' and 'y' and storing the result in the 'result' variable
result = x * y

# Printing a message indicating the multiplication of the values of the two said vectors and displaying the result
print("Multiply the values of two said vectors:")
print(result) 

m = np.arange(12).reshape((3,4))

# Printing the array 'm' representing a 3x4 matrix
print(m) 
print(m.shape) 
for i in np.nditer(m):
    print(i , end= " ")

x = np.eye(3)
print(x)

x = np.ones((10, 10))

# Setting the inner values of the matrix 'x' (excluding the borders) to 0 using slicing
x[1:-1, 1:-1] = 0

# Printing the modified matrix 'x'
print(x) 


if 'bar' in {'foo': 1, 'bar': 2, 'baz': 3}:
    print(1)
    print(2)
    if 'a' in 'qux':
        print(3)
print(4)