import numpy as np
#program to create a null vector of size 10 and update the sixth value to 11.
vector=np.zeros(10)
print(vector)

vector[5]=11
print(vector)


# Write a NumPy program to reverse an array (the first element becomes the last).
a2=np.array([1,2,3,4,5])
print("array is",a2)

#by for loop
a3=np.array([0,0,0,0,0])
n=a2.size
for i in range(n):
    a3[i]=a2[n-i-1]
print(a3)

#by slicing
reversed=a2[::-1]
print("reversed is",reversed)

#Write a NumPy program to convert an array to a floating type.
a4=np.array([1,2,3,4,5,6])
print("a4  is",a4)

float_a4=a4.astype(float)
print(float_a4)




