# Create a menu driven program for arrays having access to:
# 1. Print the array - done
# 2. Insert value at end - done
# 3. Insert value at front - done
# 4. Insert value at a given index location 
# 5. Insert value after a given value
# 6. Search value in array

#Create a menu driven program for arrays having access to:

#2. Delete value at end
#3. Delete value at front
#4. Delete value at a given index location
#5. Delete value after a given value

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
            print("\nEmpty Array :(")
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
        index = indeces[0]
        for i in range(self.N-1, index-1, -1):
                self.arr[i+1] = self.arr[i]
        self.arr[index+1] = new_value2   
        self.N = self.N+1 
        print(f"Value {new_value2} replaced successfully :)")

    def SEARCH(self, new_value3):
        indeces = np.where(self.arr == new_value3)
        index = indeces[0]
        condition = False
        for i in self.arr:
            if i == new_value3:
                condition = True
                print(f"{i} found at index {index}")
                break
        if(condition==False):
            print("Element not found")
            
    def delete_at_end(self):
        if self.N == 0:
            print("Array Underflow :(")
        else:
            self.N-=1  
            print("Delete ")        
            
    def delete_at_front(self):
        
        if self.N == 0:
            print("Array Underflow :(")
        else:
            for i in range(0, self.N-1):
                self.arr[i]=self.arr[i+1]
            self.N-=1  
            print("YAY")
    def bubble(self):
        for i in range(0,self.N-1):
            for j in range(0,self.N-i-1):
                if self.arr[j]>self.arr[j+1]:
                    temp = self.arr[j+1] 
                    self.arr[j+1] = self.arr[j]
                    self.arr[j] = temp          
            
    # def delete_at_index(self, New_values5):
    #     if self.N == 0:
    #         print("Array Underflow :(")
            
    #     elif()
    #         for i in range(0, self.N-1):
    #             self.arr[i]=self.arr[i+1]
    #         self.N-=1  
    #         print("YAY")        
    # def Bin_Search(self, val_5):
        
            

SIZE = 10
arraymanager = ArrayManager(SIZE)
while(1):
    print("===== Array Manager =====")
    print("1. Print the array")
    print("2. Insert value at end")
    print("3. Insert value at front")
    print("4. Insert value at a given index location")
    print("5. Insert value after a given value")
    print("6. Search value in array")
    print("7. delete value at end")
    print("8. delete value at front")
    print("9. for bubble sort")
    # print("9 .delete value at index")
    
    
    
    ch = int(input("Enter your choice: "))

    if(ch==1):
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
    # elif(ch==9):
    #     New_values5 = int(input("Enter Index value :"))
    #     arraymanager.delete_at_index(New_values5)    
    elif(ch==8):
        val_5 = int(input("Enter a value to search : "))
        arraymanager.Bin_Search()
    elif(ch==9):
        #val_6 = int(input("Enter a value to search : "))
        arraymanager.bubble()          
    else:
        print("\n'Invalid Input' :(")



