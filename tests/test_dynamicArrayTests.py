import sys
from pathlib import Path

# Add /src to Python's import path so tests can import your module
sys.path.append(str(Path(__file__).resolve().parents[1] / "src"))

from dynamicArray import dynamicArray

def test_giveSize():
    dynamic_Array = dynamicArray(5)
    for i in range (4):
        dynamic_Array.insert_Element(3,0)
    assert dynamic_Array.give_Size() == 4