#! myenv\Scripts\python.exe

import numpy as np 

class dynamicArray:
    # variables for sizing
    CAPACITY = 15
    SIZE = 0   
    
    #create the dynamic array
    def __init__(self,capacity = 15):
        self.size = 0
        self.capacity = capacity
        self.data = [None] * capacity
    
   
            
    # method to return the size     
    def give_Size(self):
        return self.size
    
     # print the array
    def print_dArray(self):
        print(self.data)
    
    def append_Element (self, element_1):
        current_Size = self.give_Size()
        
        if(current_Size > self.capacity):
            print("The current size:", current_Size, " exceeds the capacity:", self.capacity, ".Resizing by one\n")
            self.capacity += 1
            self.data[-1] = element_1
            self.size += 1
            print ("New size is: ", self.capacity)
        else :
            print("\nCurrent size:", self.size,". Current capacity:", self.capacity)
            self.data[current_Size] = element_1
            self.size += 1
            print("New size:", self.size,". Current capacity:", self.capacity)

            
            