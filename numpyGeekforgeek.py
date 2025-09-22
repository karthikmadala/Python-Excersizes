import numpy as np

# Create an empty array of shape (3, 4)
empty_array = np.empty((3,4))
print("Empty Array:\n", empty_array)

# Create a full array of shape (3, 3) filled with the value 5
full_array = np.full((3, 3), 5)
print("Full Array:\n", full_array)

array = np.ones(5)
print(array)

ones_array_2d = np.ones((3, 4))
print(ones_array_2d)

ones_int_array = np.ones(4 , dtype=int)

print(ones_int_array)

ones_array_3d = np.ones((2, 3, 4)) # 2 shape 3 row 4 col

print(ones_array_3d)



