#! myenv\Scripts\python.exe

#################################################################################################
# Author: Gio Adaya

# My own dynamic array class. Meant to solidify my understanding of data structures while refreshing
# up on Python.

#################################################################################################

class dynamicArray: 
    
    #################################################################################################
    # Function Name: init
    
    # Purpose: Initializes the dynamicArray
    #################################################################################################
    def __init__(self,capacity = 15):
        self.size = 0
        self.capacity = capacity
        self.data = [None] * capacity
    
    #################################################################################################
    # Function Name: give_Size
    
    # Purpose: Returns the size of the array
    #################################################################################################
    def give_Size(self):
        return self.size    
    
    #################################################################################################
    # Function Name: print_dArray
    
    # Purpose: Prints the Array 
    #################################################################################################
    def print_dArray(self):
        print(self.data[0:self.size])
    
    #################################################################################################
    # Function Name: resize_Array
    
    # Purpose: Helper function to resize the array when needed. Used in multiple functions
    #################################################################################################
    def resize_Array(self, curr_Size):
        new_Capacity = self.capacity * 2
        new_Array = [None] * new_Capacity
        for i in range(curr_Size):
            new_Array[i] = self.data[i]
        return new_Array, new_Capacity
    
    #################################################################################################
    # Function Name: append_Element
    
    # Purpose: Adds an element to the end of the dynamic array. If the size of the array is at max
    #          capacity, then it is resized through creating a new, larger array, copying the old
    #          array, then finally adding the element at the last index. If the size of the array
    #          is not at max capacity, then we simply store the element at the end of the array.
    #################################################################################################
    def append_Element (self, element_1):
        
        if self.size >= self.capacity:
            
            print("\nThe current size:", self.size, "is at capacity:", self.capacity, ". Resizing")
            new_Array, new_Capacity= self.resize_Array(self.size)
            
            new_Array[self.size] = element_1
            self.data = new_Array
            self.size +=1
            self.capacity = new_Capacity
            
            print ("New size is: ", self.size)
            print("size, capacity:", self.size, self.capacity)
        else :
            
            print("\nCurrent size:", self.size,". Current capacity:", self.capacity)
            self.data[self.size] = element_1
            self.size += 1
            print("New size:", self.size,". Current capacity:", self.capacity)            
            
    #################################################################################################
    # Function Name: insert_Element
    
    # Purpose: Inserts an element at the specified index. The index must be valid, meaning it cannot 
    #          be at an index greater than the size
    #################################################################################################
    def insert_Element(self, element, index):
        if index < 0 or index > self.size:
            print("Invalid index.")
            return 

        if self.size == self.capacity:
            new_Array, new_Capacity = self.resize_Array(self.size)
            self.data = new_Array
            self.capacity = new_Capacity

        for i in range(self.size - 1, index - 1, -1):
            self.data[i + 1] = self.data[i]

        self.data[index] = element

        self.size += 1

        self.print_dArray()
                
    #################################################################################################
    # Function Name: remove_Here
    
    # Purpose: Removes an element at a given index. If the index is invalid, we return and let the
    #          user know. Otherwise, we remove the element, and shift the elements to the left that 
    #          are to the right of the element at the specified index
    #################################################################################################
    def remove_Here(self, index):
        if index < 0 or index >= self.size:
            print("Invalid index\n")
            return
        else:
            for i in range(index + 1, self.size, 1):
                self.data[i - 1] = self.data[i]
            self.size-=1
    
    #################################################################################################
    # Function Name: get_Element
    
    # Purpose: Returns the element at the specified index
    #################################################################################################
    def get_Element(self, index):
        
        if index < 0 or index >= self.size:
            print("Invalid Index\n")
            return
        else:
            print("The value at index", index ,"is", self.data[index])
            return self.data[index]
    
    #################################################################################################
    # Function Name: my_Set
    
    # Purpose: Sets the value the user specifies into the index specified. The previous value at that
    #          index gets replaced
    #################################################################################################
    def my_Set(self, index, element):
        
        if index < 0 or index >= self.size:
            print("Invalid Index\n")
            return
        else:
            self.data[index] = element
            
    #################################################################################################