# Joining Numpy Arrays
print("\n------$ Joining Numpy Arrays $--------\n")

# Joining Numpy Arrays : vstack()  [Vertical Stack]
import numpy as np
n1 = np.array([1,2,3,4,5])
n2 = np.array([6,7,8,9,10])

print("NumPy Arrays : vstack()")
print(np.vstack((n1,n2)))

# Joining Numpy Arrays : hstack()   [Horizontal Stack]
print("\nNumPy Arrays : hstack()")
print(np.hstack((n1,n2)))

# Joining Numpy Arrays : column_stack()     [
print("\nNumPy Arrays : column_stack()")
print(np.column_stack((n1,n2)))
