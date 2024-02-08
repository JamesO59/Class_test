
import numpy as np

arr = np.array([1,2,3,4,5,6])
g = len(arr)
lower_bound = 0
upper_bound = g-1

val = int(input("Enter a number to search the element in array : "))

def Bin_search(arr, val):
    BEG = lower_bound
    END = upper_bound
    POS = -1
    while BEG<=END:
        MID = int((BEG+END)/2)
        if(arr[MID] == val):
            print(f"\nElemet found at {MID}th index")
            POS = MID
            break
        elif(arr[MID]>val):
            END = MID - 1
        else:
            BEG = MID + 1
    if(POS==-1):
        print("Value not found in array :(")  
                  
Bin_search(arr, val)            
            
#####

import numpy as np

def transpose(matrix):
    result = np.zeros((matrix.shape[1], matrix.shape[0]))
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            result[j][i] = matrix[i][j]
    return result

# Example usage:
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Original Matrix:")
print(matrix)

transposed_matrix = transpose(matrix)
print("\nTransposed Matrix:")
print(transposed_matrix)

 
                    