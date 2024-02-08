import numpy as np

matrix = np.array([[1,5,7], [3,4,2], [1,9,7]])

def Transpose(matrix):
    result = np.zeros((matrix.shape[1], matrix.shape[0]))
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            result[j][i] = matrix[i][j]
    return result


g = Transpose(matrix)

print(matrix, ": Original Matrix")        
print(g, ": Original Matrix")
        
