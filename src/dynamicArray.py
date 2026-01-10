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
    
    # print the array
    def print_dArray(self):
        for item in range(self.data):
            print(self.data)
            
    # method to return the size     
    def give_Size(self):
        return self.size
    
    def append_Element (self, element_1):
        current_Size = self.give_Size()
        
        if(current_Size > self.capacity):
            self.capacity += 1
            self.data[-1] = element_1
        else :
            self.data[self.size] = element_1
            self.size += 1
            
            