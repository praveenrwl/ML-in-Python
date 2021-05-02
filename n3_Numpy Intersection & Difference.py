# Numpy Intersection and Difference :

# INTERSECTION IN NUMPY :
import numpy as np
n1 = np.array([10,20,30,40,50,60])
n2 = np.array([50,60,70,80,90])

print("\nNumPy Intersection: ")
print(np.intersect1d(n1,n2))

# DIFFERENCE IN NUMPY :

print("\nNumPy Difference: ")
print(" #a", np.setdiff1d(n1,n2))

print(" #b",np.setdiff1d(n2,n1))

