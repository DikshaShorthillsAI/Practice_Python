A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]
def matrix_addition(A, B):  # Matrix addition
    result = []
    for i in range(len(A)):  # Iterate over rows
        row = []
        for j in range(len(A[0])):  # Iterate over columns
            row.append(A[i][j] + B[i][j]) 
        result.append(row)
    return result
print("Matrix Addition : ", matrix_addition(A, B))  
def matrix_subtraction(A, B):   # Matrix subtraction
    result = []
    for i in range(len(A)):
        row = []
        for j in range(len(A[0])):
            row.append(A[i][j] - B[i][j])
        result.append(row)
    return result
print("Matrix Subtraction : ", matrix_subtraction(A, B)) 
def matrix_multiplication(A, B):  # Matrix multiplication
    result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]
    for i in range(len(A)):  # Iterate over rows of A
        for j in range(len(B[0])):  # Iterate over columns of B
            for k in range(len(B)):  # Iterate over rows of B
                result[i][j] += A[i][k] * B[k][j]
    return result
print("Matrix Multiplication : ", matrix_multiplication(A, B)) 
def transpose(matrix):      # Matrix transpose
    result = [[0 for _ in range(len(matrix))] for _ in range(len(matrix[0]))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            result[j][i] = matrix[i][j]  # Swap rows and columns
    return result
matrix = [[1, 2], [3, 4], [5, 6]]
print("Matrix Transpose : ", transpose(matrix)) 
def scalar_multiplication(matrix, scalar):     # Scalar multiplication
    result = []
    for row in matrix:
        result.append([scalar * element for element in row])
    return result
matrix = [[1, 2], [3, 4]]
scalar = 3
print("Scalar Matrix Multiplication : ", scalar_multiplication(matrix, scalar))  

