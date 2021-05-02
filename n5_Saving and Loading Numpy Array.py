# Saving and Loading Numpy Array:

# Saving Numpy Array :
import numpy as np
n1 = np.array([10,20,30,40,50,60])
np.save('my_numpy',n1)


# Loading Numpy Array :
n2 = np.load('my_numpy.npy')
print(n2)