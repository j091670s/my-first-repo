import dynamicArray
from dynamicArray import dynamicArray

my_dynamic_Array = dynamicArray(5)

for i in range (5):
    my_dynamic_Array.append_Element(1)


my_dynamic_Array.print_dArray()
my_dynamic_Array.append_Element(2)
my_dynamic_Array.print_dArray()
print("after insert operations:\n")
my_dynamic_Array.insert_Element(3,0)
my_dynamic_Array.insert_Element(2,2)
my_dynamic_Array.insert_Element(4,3)
currentSize = my_dynamic_Array.give_Size()
my_dynamic_Array.insert_Element(4,currentSize)
my_dynamic_Array.insert_Element(4,my_dynamic_Array.give_Size() + 1)
my_dynamic_Array.insert_Element(4,-1)
my_dynamic_Array.remove_Here(1)
my_dynamic_Array.print_dArray()
value = my_dynamic_Array.get_Element(2)
my_dynamic_Array.my_Set(0,67)
my_dynamic_Array.print_dArray()





