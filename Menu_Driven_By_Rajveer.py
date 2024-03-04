
import numpy as np
class ArrayManager:
    def __init__(self, SIZE):#, value, LOC):
        self.arr=np.zeros(SIZE) 
        self.N=0
        #self.SIZE = SIZE
        #self.Value = value
        #self.LOC = LOC

    def print_array(self):
        if self.N==0:
            print("\nEmpty Array :(\n") 
        else:
            for i in range(0, self.N):
                print(self.arr[i])   

    def insert_at_end(self, SIZE, Value):
        if(self.N==SIZE):
            print("\nArray Overflow !!")
        else:
            self.arr[self.N]=Value
            self.N=self.N+1
            print("\nValue added at end successfuly :)")
 
    def insert_at_front(self, SIZE, Value):
        if self.N == SIZE:
            print("\nArray Overflow !!")
        else:
            for i in range(self.N-1, -1, -1):
                self.arr[i+1] = self.arr[i]
            self.arr[0] = Value
            self.N += 1
            print("\nValue added at front successfully :)")

    def insert_at_index(self, P, new_value):
        if self.N == SIZE: 
            print("\nArray Overflow !!")
        elif(P<0 or P>self.N):
            print("Invalid input")    
        elif(P==self.N):
            self.arr[P]=new_value
            self.N +=1
        else:   
            for i in range(self.N-1, P-1, -1):
                self.arr[i+1] = self.arr[i]
            self.arr[P] = new_value
            self.N += 1 
            print("\nValue added at the given index successfully :)")

    def insert_after_value(self, existing_value, new_value2): 

        indeces = np.where(self.arr == existing_value)
        index = indeces[0][0]
        for i in range(self.N-1, index-1, -1):
                self.arr[i+1] = self.arr[i]
        self.arr[index+1] = new_value2   
        self.N = self.N+1 
        print(f"\nValue {new_value2} replaced successfully :)\n")

    def SEARCH(self, new_value3):
        indeces = np.where(self.arr == new_value3)
        index = indeces[0]
        condition = False
        for i in self.arr:
            if i == new_value3:
                condition = True
                print(f"\n{i} found at index {index}\n")
                break
        if(condition==False):
            print("Element not found")
            
    def delete_at_end(self):
        if self.N == 0:
            print("Array Underflow :(")
        else:
            self.N-=1  
            print(f"{self.arr[self.N]} value deleted successfully :)")        
            
    def delete_at_front(self):
        
        if self.N == 0:
            print("Array Underflow :(")
        else:
            print(f"{self.arr[0]} deleted successfully :)")       
            for i in range(0, self.N-1):
                self.arr[i]=self.arr[i+1]
            self.N-=1  
            
    def delete_the_value(self, New_values6):
        if self.N == 0:
            print("Array Underflow :(")
        else:
            indeces = np.where(self.arr == New_values6)
            index = indeces[0][0]
            condition = False
            print(f"{self.arr[index+1]} value deleted successfully :)") 
            for i in range(index+2, self.N):
                condition = True
                self.arr[i-1]=self.arr[i]
            self.N-=1     
            if(condition==False):
                print("Element not found")

    def bubble(self):
        for i in range(0,self.N-1):
            for j in range(0,self.N-i-1):
                if self.arr[j]>self.arr[j+1]:
                    temp = self.arr[j+1] 
                    self.arr[j+1] = self.arr[j]
                    self.arr[j] = temp     
            

SIZE = 10
arraymanager = ArrayManager(SIZE)
while(1):
    print("===== Array Manager =====")
    print("0. To Exit")
    print("1. Print the array")
    print("2. Insert value at end")
    print("3. Insert value at front")
    print("4. Insert value at a given index location")
    print("5. Insert value after a given value")
    print("6. Search value in array")
    print("7. Delete value at end")
    print("8. Delete value at front")
    print("9. For bubble sort")
    print("10. Delete the given value")
    
    
    
    ch = int(input("Enter your choice: "))
    if(ch==0):
        print("\nExiting ... bye :)\n")
        break
    elif(ch==1):
        arraymanager.print_array()
    elif(ch==2):
        Value = int(input("\nEnter a value to add at end: "))
        arraymanager.insert_at_end(SIZE, Value)        
    elif(ch==3):
        Value2 = int(input("Enter a value to add at front: "))
        arraymanager.insert_at_front(SIZE, Value2)  
    elif(ch==4):
        P = int(input("Enter index : "))
        new_value = int(input("Enter New Value : "))
        arraymanager.insert_at_index(P, new_value)    
    elif(ch==5):
        existing_value = int(input("Enter existing value : "))
        new_value2 = int(input("Enter New Value : "))
        arraymanager.insert_after_value(existing_value, new_value2)    
    elif(ch==6):
        new_value3 = int(input("Enter Value to search : "))
        arraymanager.SEARCH(new_value3)
    elif(ch==7):
        arraymanager.delete_at_end()           
    elif(ch==8):
        arraymanager.delete_at_front()  
    elif(ch==9):
        arraymanager.bubble()        
    elif(ch==10):
        New_values6 = int(input("Enter Index value :"))
        arraymanager.delete_the_value(New_values6)        
    else:
        print("\n'Invalid Input' :(")


"""
#2
# Lab Assignment 3 :
# 1. Implement binary search
        
def Binary_search(arr, user_input):
    hight_bound =  len(arr)-1
    low_bound= 0
    while  (low_bound <= hight_bound):
        mid = (low_bound + hight_bound)//2
        if arr[mid] == user_input:
            return mid
        elif arr[mid] < user_input:
            lower_bound  = mid - 1
        else:
            hight_bound  = mid + 1    
    return -1    



user_input = int(input("Enter a value to search in an array: "))
arr = ([1,2,3,4,5,6,10])        

result = Binary_search(arr, user_input)

if  result !=-1:
    print(f"Your element found  at index position {result}")
else:
    print("Element not found")    



# 2. Find transpose of a matrix.

import numpy as np

arr = np.array([[1,2],[3,4]]) 
print(f"\n {arr} :Default matrix\n")
result = np.empty((len(arr[0]), len(arr)), dtype=arr.dtype) # datatype mismatch like int64 and int32

for i in range(len(arr)):
    for j in range(len(arr[0])):
        result[j][i] = arr[i][j]

print(f"\n{result} : is the  Transposed Matrix \n ")  


# 3. Find the sum of two matrices.
import numpy as np

arr = np.array([[1,2],[3,4]]) 
arr2 = np.array([[5,6],[7,8]]) 
print(f"\n {arr} : matrix 1\n")
print(f"\n {arr2} : matrix 2\n")
result2 = np.empty((len(arr[0]), len(arr)), dtype=arr.dtype)

for  i in range(len(arr)):
    for  j in range(len(arr[0])):
        result2[i][j] = arr[i][j] + arr2[i][j]

print(f"{result2} : is the sum of the two matices")        


# 4. Multiply two matrices.
import numpy as np

arr = np.array([[1, 2],
                [3, 4]])
arr2 = np.array([[5, 6],
                 [7, 8]])
print(f"\n{arr} <--- is the matrix 1\n")
print(f"\n{arr2} <--- is the matrix 2\n")
result = np.zeros((len(arr), len(arr[0])), dtype=arr.dtype)
for i in range(len(arr)):
    for j in range(len(arr2[0])):
        for k in range(len(arr2)):
            result[i][j] += arr[i][k] * arr2[k][j]

print(f"{result} <--- is the product of  matrix 1 and 2.\n")
"""

"""
# Lab assignment 4

# Insertion sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        j=i
        while arr[j-1]>arr[j] and j>0:
            arr[j-1], arr[j] = arr[j], arr[j-1]
            j-=1
            
arr = [6,5,3,1,2,7,4,8,9]
print(f"{arr} : original array")
insertion_sort(arr)
print(f"\n{arr} : is the sorted array")



# Selection sort

import numpy as np

def selection_sort(arr):
    for i in range(0, len(arr) - 1):
        current_min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[current_min_idx]:
                current_min_idx = j
        
        arr[i], arr[current_min_idx] = arr[current_min_idx], arr[i]

arr = [6,5,3,1,2,7,4,8,9]
selection_sort(arr)
print(arr)

"""

"""
# Lab assignment 5

ct = 4

import numpy as np
arr = np.array([1, 2, 4, 5])
flag = -1
se = int(input("Enter a number to find : "))
for i in range(0, len(arr)):
    if(arr[i]==se):
        print(f'Element {se} found at  index {i}')
        flag = 1
        ct = ct + 5
        break
    else:
        ct = ct + 2
        pass
if flag == -1:
    print("Element not found")
    ct = ct + 2
ct = ct + 1    

print(f"\nNumber of comparisons made are {ct}")

best_case = 10
average_case = (arr[0]+arr[1]+arr[2]+arr[3])/len(arr)
worst_case = 16
print(f"\nBest case time complexity is O({best_case})")
print(f"Average case time complexity is O({average_case})")
print(f"Worst case time complexity is O({worst_case})")

"""
