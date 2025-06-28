import numpy as np
#Q1.   Combining  a one and two D array
arr=np.array([1,2,3],ndmin=2)
arr2D=np.array([[4,5,6],[7,8,9]])
arr3=np.concatenate((arr,arr2D))
print(arr3)

#Q.2  flattten a 2d numpy array into 1d array
arr2D=np.array([[4,5,6],[7,8,9]])
flatten_array=arr2D.flatten()       # we can use both flatten and ravel for converting any D arry in 1D
flatten_array1=arr2D.ravel()
print(flatten_array)
print(flatten_array1)


#Q.3  reverse a numpy array
a=np.array([1,2,3,4,5,6,80])
print("Reversed is :",a[::-1])


#Q.4 Practicing various operations like min,max and many more
a2=np.array([[4,5,6],[7,8,9]])
print("max is :",a2.max())
print("min is :",a2.min())

print("shape of array rows,columns :",a2.shape)

print("element:",a2[1,2])

sum=0
for x in a2:
    for y in x:
        sum+=y
print("sum is :",sum)










