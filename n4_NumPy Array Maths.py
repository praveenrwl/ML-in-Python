# NumPy Array Mathematics :

# Addition of NumPy Arrays :
import numpy as np
n1 = np.array([1,2,3])
n2 = np.array([4,5,6])

print("\n# NumPy Addition: ")
print(np.sum([n1,n2]))
print(np.sum([n1,n2], axis=0))
print(np.sum([n1,n2], axis=1))

# Subtraction of NumPy Arrays :
x = n1-n2
print("\n# NumPy Subtraction:\n",x)

# Multiplication of NumPy Arrays :
y = n1*n2
print("\n# NumPy Multiplication:\n",y)

# Division of NumPy Arrays :
z = n1/n2
print("\n# NumPy Division:\n",z)

# Mean of NumPy Arrays :
mean = np.array([2,4,5,8,9,1,4,6])
print("\n# NumPy Arrays Mean: \n", np.mean(mean))

# Median of NumPy Arrays :
med = np.array([11,32,3,4,53,12,32,11,7,9])
print("\n# NumPy Arrays Median: \n", np.median(med))

# Standard Deviation of NumPy Arrays :
sd= np.array([1,12,32,23,21,4,7,26,19])
print("\n# NumPy Arrays Standard Deviation: \n", np.std(sd))