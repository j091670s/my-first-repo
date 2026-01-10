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
    #################################################################################################

    # method to return the size     
    def give_Size(self):
        return self.size
    #################################################################################################
    
    
    # print the array
    def print_dArray(self):
        print(self.data[0:self.size])
    #################################################################################################
    
    # append element to the end of the array
    def append_Element (self, element_1):
        current_Size = self.give_Size()
        
        if(current_Size >= self.capacity):
            
            print("\nThe current size:", current_Size, " exceeds the capacity:", self.capacity, ".Resizing")
            new_Capacity = self.capacity * 2
            new_Array = [None] * new_Capacity
            for i in range(current_Size):
                new_Array[i] = self.data[i]
            
            new_Array[current_Size] = element_1
            self.data = new_Array
            self.size +=1
            self.capacity = new_Capacity
            
            print ("New size is: ", self.size)
            print("size, capacity:", self.size, self.capacity)
        else :
            
            print("\nCurrent size:", self.size,". Current capacity:", self.capacity)
            self.data[current_Size] = element_1
            self.size += 1
            print("New size:", self.size,". Current capacity:", self.capacity)

    #################################################################################################
            
    # insert is next, then remove, get, and set