#About Numpy
'''Python library is a collection of functions and methods that allows you to perfrom many actions without writing of codes'''
'''NUMPY stands for NUMERICAL PYTHON and is the core library for numeric and scientific computing '''
'''It consists of multi dimensional array objects and a collection of routines for processing those arrays '''

# Single Dimensional Array
import numpy as np
n1 = np.array([10,20,30,40,50])
print("#1 Single Dimensional Array :\n ", n1)
print(type(n1), "\n")

# Multi Dimensional Array
import numpy as np
n2 = np.array([[1,2,3,4,5],[11,12,13,14,15]])
print("#2 Multi Dimensional Array :\n", n2)

# Initializing NumPy array with zeroes :
# 1
import numpy as np
n3 = np.zeros((1,2))
print("\n#3 Initializing NumPy array with zeroes :\n #A\n", n3)

# 2
n4 = np.zeros((5,5))
print("\n #B\n", n4)

# Initializing NumPy array with same number :
# Will make matrix >>
n5 = np.full((3,3),10)
print("\n#4 Initializing NumPy array with zeroes :\n", n5)

# Initializing NumPy array within a range :
n6 = np.arange(11,21)
print("\n#5 Initializing NumPy array within a range :\n", n6)

n7 = np.arange(10,51,5)
print("\n#6 Initializing NumPy array within a range :\n", n7)

# Initializing NumPy array with random numbers :
n8 = np.random.randint(1,100,5)
print("\n#7 Initializing NumPy array with random numbers :\n", n8)

# Check the shape of NumPy arrays :
n9 = np.array([[1,2,3],[4,5,6]])
print("\n#8 Check the shape of NumPy arrays:\n #A\n", n9)
n9.shape
print("\n #B\n", n9)
n9.shape = (3,2)
print("\n #C\n", n9)
