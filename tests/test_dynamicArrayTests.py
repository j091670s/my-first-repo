import sys
from pathlib import Path

# Add /src to Python's import path so tests can import your module
sys.path.append(str(Path(__file__).resolve().parents[1] / "src"))

from dynamicArray import dynamicArray


#################################################################################################
# Test Name: test_giveSize
    
# Purpose: Testing give size returns the correct size of the array after inserting elements
#################################################################################################
def test_giveSize():
    dynamic_Array = dynamicArray(5)
    for i in range (4):
        dynamic_Array.insert_Element(3,0)
    assert dynamic_Array.give_Size() == 4

#################################################################################################
# Test Name: test_appendElement
    
# Purpose: Testing that append_Element properly adds an element to the end of the array. If the 
#          array is not full, then it adds the element to the end, otherwise, it resizes and adds
#          the element.
#################################################################################################
def test_appendElement():
    dynamic_Array = dynamicArray(5) # capacity set to 5, should resize once full
    for i in range (4):
        dynamic_Array.insert_Element(3,0)
    dynamic_Array.append_Element(2)
    assert dynamic_Array.give_Size() == 5
    dynamic_Array.append_Element(5)
    assert dynamic_Array.give_Size() == 6

    