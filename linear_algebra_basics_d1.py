# 1/20/25 
import numpy as np 

# Create an array in numpy - Basic LA operation of summing 
a = np.array([2, 4, 6]) 
b = np.array([1, 3, 5]) 
print("----------------------------------")
print(a)
print(b)
print(a + b) 

# Basic LA operation for multiplying scalar with vectors
a = np.array([3, 7])
b = 4
print("----------------------------------")
print(a)
print(a * b)

# Basic Matrix multiplication element-wise
# Can create explicitly create a column or row vector using np.newaxis
# row vector would require np.newaxis in the first column
a = np.array([[1, 2], [3, 4]])
# Column vector
b = np.array([2, 3])
print("----------------------------------")
print(a)
print(b)
print(a * b)
print(np.sum(a * b, axis = 1))
# Should only use dot on vectors in this case it works bc of how np's broadcasting works
print(a.dot(b))

# Understanding axis
a = np.array([[1, 2], [3, 4]])
print("----------------------------------")
print(a)
# Axis = 0 sums along the columns
print("Axis = 0: ", np.sum(a, axis = 0))
# Axis = 1 sums along the rows
print("Axis = 1: ", np.sum(a, axis = 1))
