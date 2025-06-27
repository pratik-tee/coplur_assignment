import numpy as np
#array with random values

a=np.random.rand(3,1)
print(a)

#(4x2) empty and a full numpy array
empty_array=np.empty((4,2))
print("array is \n",empty_array)

a2=np.full((4,2),5)
print("the full array is \n",a2)

#(3x5) array with zeroes
a3=np.zeros((3,5))
print("array with zeroes is \n",a3)

#4x3x2 arry with eith ones
a4=np.ones((4,3,2))
print(a4)





