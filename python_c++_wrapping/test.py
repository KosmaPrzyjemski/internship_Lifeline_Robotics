"""
Creating a wrapper for a c++ code.
The c++ code is a simple addition function called "hw1".
"""

# We want to call the c++ function from Python as :
from hw import hw1
r1=1.2
r2=-1.2
s=hw1(r1,r2)
print(s)

"""
Python is written in C and every object in Python is represented by a C struct PyObject.
Wrapper code converts between PyObject variables and plain C variables, for instance here :
from PyObject r1 and r2 to double, and in the opposite way from double to PyObjec.
Once compilet it can be loaded as a Python module (just like a standard Python code).
"""
