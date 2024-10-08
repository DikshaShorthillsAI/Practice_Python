import numpy as np

# Creating a matrix
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# Matrix addition
print(np.add(A, B))  
                    

# Matrix subtraction
print(np.subtract(A, B))  

# Matrix multiplication (element-wise)
print(np.multiply(A, B)) 

# Matrix multiplication (dot product)
print(np.dot(A, B)) 

# Transpose of a matrix
print(np.transpose(A)) 

# Scalar multiplication
print(3 * A) 
