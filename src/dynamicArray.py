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
    
    # resize helper function
    def resize_Array(self, curr_Size):
        new_Capacity = self.capacity * 2
        new_Array = [None] * new_Capacity
        for i in range(curr_Size):
            new_Array[i] = self.data[i]
        return new_Array, new_Capacity
    
    # append element to the end of the array
    def append_Element (self, element_1):
        current_Size = self.give_Size()
        
        if(current_Size >= self.capacity):
            
            print("\nThe current size:", current_Size, "is at capacity:", self.capacity, ". Resizing")
            new_Array, new_Capacity= self.resize_Array(current_Size)
            #new_Capacity = self.capacity * 2
            #new_Array = [None] * new_Capacity
            #for i in range(current_Size):
                #new_Array[i] = self.data[i]
            
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
    def insert_Element(self, element, array_Index):
        current_Size = self.give_Size()

        if array_Index < 0 or array_Index > current_Size:
            print("Invalid index.")
            return
        if array_Index == self.size: #appending 
            
            if current_Size == self.capacity:
                new_Array, new_Capacity = self.resize_Array(current_Size)
                #new_Capacity = self.capacity * 2
                #new_Array = [None] * new_Capacity
                #for i in range(current_Size):
                    #new_Array[i] = self.data[i]
            
                new_Array[current_Size] = element
                self.data = new_Array
                self.size +=1
                self.capacity = new_Capacity
                
            else:
                
                self.data[array_Index] = element
                self.size+=1
                
        elif array_Index == 0:
            
            current_Capacity = self.capacity
            
            if current_Size == current_Capacity:
                new_Array,new_Capacity = self.resize_Array(current_Size)
                #new_Capacity = self.capacity * 2
                #new_Array = [None] * new_Capacity
                #for i in range(current_Size):
                    #new_Array[i] = self.data[i]
                    
                for i in range(current_Size - 1, array_Index - 1, -1):
                    new_Array[i + 1] = self.data[i]
            
                new_Array[array_Index] = element
                self.data = new_Array
                self.size +=1
                self.capacity = new_Capacity
                    
            else:      
                new_Array = [None] * current_Capacity
                for i in range(current_Size):
                    new_Array[i] = self.data[i] 
                     
                for i in range(current_Size - 1, array_Index - 1, -1):
                    new_Array[i + 1] = self.data[i]
            
                new_Array[array_Index] = element
                self.data = new_Array
                self.size +=1
                
        else :
            current_Capacity = self.capacity
            if current_Size ==  current_Capacity:
                new_Array, new_Capacity = self.resize_Array(current_Size)
                #new_Capacity = self.capacity * 2
                #new_Array = [None] * new_Capacity
                #for i in range(current_Size):
                    #new_Array[i] = self.data[i]
            
                for i in range(current_Size - 1, array_Index - 1, -1):
                    new_Array[i + 1] = new_Array[i]
                    
                new_Array[array_Index] = element
                self.data = new_Array
                self.size+=1
                self.capacity = new_Capacity
            else:
                
                new_Array = [None] * current_Capacity
                for i in range(current_Size):
                    new_Array[i] = self.data[i]
                    
                for i in range(current_Size - 1, array_Index - 1, -1):
                    new_Array[i + 1] = new_Array[i]
                    
                new_Array[array_Index] = element
                self.data = new_Array
                self.size+=1
                
                
        self.print_dArray()
                
