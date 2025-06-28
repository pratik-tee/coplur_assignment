import numpy as np

print(np.__version__)

a=np.array([1,2,3])              #1d array
print(a)

print(type(a))

a2=np.array([[1,2,3],[4,5,6]])          #2d array
print(a2)
print(type(a2))       
print(a2.dtype)        #for checking the data type

a3=np.array(['A','B','C'])
print("data type is", a3.dtype)      #unicode string

try:
  a4=np.array([7,8,9,'A'],dtype='i4')
  print(a4)
  print(a4.dtype)

except ValueError:
 print("Value error")
 
a4=np.ones(5)
print(a4)

a5=np.zeros((5,4))
print(a5)

a6=np.ones((5,4),order='F')       #F and C stands for different memory layout
print(a6)

a7=np.arange(1,11,2)       #(start,stop,step) in arrange function
print('Array after arrange',a7)

a8=np.linspace(0,5,num=5,endpoint=False)     # it divides values in given range
print("Linespace",a8)                        #endpoint false represent that last number is not included in that

a9=np.linspace(0,5,num=5,retstep=True)     #it gives us also steps  like in this exp step is 1.25
print("Linespace2",a9)

random_float=np.random.rand(3,2,4)                 #it gives us random values in 0 to 1   #3d array   we can also create 2d and 1d array
print("Random values are",random_float)


empty_array=np.empty((2,3))                    #it create the empty array  
print("array is \n",empty_array)
print(type(empty_array))

a10=np.full((2,3),'A')                             #it create an afray with assigned value 
print("array with assigned value:\n",a10)

a11=np.array([7,8,9,5,6])                          #accessing the 1D array element
print("The element is: ",a11[2])

print("the sum is: ",a11[3]+a11[4])


a12=np.array([[7,5,6],[4,2,8]])                       #accessing the 2D array element
print("the element is: ",a12[1,2])


a13=np.array([[[1,2,3],[2,4,5]],[[7,8,9],[4,5,6]],[[10,11,12],[13,14,15]]])   #accessing the 3D array element
print(a13)
print("the element is :",a13[1,0,2])

print("e:",a12[-1,-3])                    #accessing by negative range

print("el:",a13[-1,-1,-3])

#slicing in array
print("k",a11[1:4])      #slicing in 1d array
print("d",a11[::2])

print(a12[1,1:3])

print(a12[0,1:3])


a14=np.array([[7,8,9,10,11],[4,5,6,12,13]])
print(a14[:,1:4])                                   # to select all rows
print(a14[0:2,1:4])                                  # to select particular rows (for slicing 2d array)




















