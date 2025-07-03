import numpy as np
arr=np.array([
     [[1,2,3,8],
      [4,5,6,9],
      [7,8,9,10]],
     [[11,12,13,24],
      [14,15,16,25],
      [17,18,19,26]],
     
]   )
print(arr[0,2,3])
print("3d array is \n",arr)
print("shape of array is\n",arr.shape)

a2=np.zeros((2,3,4))
print(a2)

a3=np.array([7,8,9,4,5,6])
z=a3.copy()
print("copy of a3 is:",z)
a3[0]=34
print(z)

k=a3.view()
print(k)
a3[1]=956
print(k)

x=a3.copy()
y=a3.view()
print(x.base)                #it gives none because it creates a new array
print(y.base)                 #there is y that will represent base

a4=np.array([6,6,8,5],ndmin=5)            # ndmin is used to create specified dimension of an array 
print(a4)
print("dimension of array is \n",a4.ndim) 

a5=np.array([1,2,3,4,5,6,4,5,6,10,11,12])    #it will create a 4x3 array
resp=a5.reshape(4,3)
print(resp)

a6=np.array([[1,2,3],[4,6,7]])
newarr=a6.reshape(-1)                    #2d into 1d
print(newarr)

#loop in  numpy

a7=np.array([4,5,6,6])
for elements in a7:
    print(elements)
    
print(type(elements))

a8=np.array([[3,4,56,7],[34,75,3,5]])
for element in a8:
    print(element)
    for ele in element:
        print(ele)


arr1=np.array([
     [[1,2,3,8],
      [4,5,6,9],
      [7,8,9,10]],
     [[11,12,13,24],
      [14,15,16,25],
      [17,18,19,26]],
     
])  

for x in arr1:
    print(x)
    for y in x:
        print(y)
        for z in y:
            print(z)   
print("end of for loop")           #for accessing all the elements of an array  by an single loop
for x in np.nditer(arr1):
     print(x)     

a9=np.array([[3,4,56,7],[34,75,3,5]])           # to convert into 1D array by ravel() functions
print(a9.ravel())

print(a9.min(1),a9.max(1))            # to find max and min in array

print("sum  is",a9.sum(0))             #if we pass 0 then it get sum of all columns wise elements
print("sum  is",a9.sum(1))              # and if we pass 1 then it get sum of all rows wise elements
   
print(np.sqrt(a9))                    #to find sqrt of an whole array

a=np.array([[1,2],[4,5]])                    
b=np.array([[56,755],[43,56]])
print(a+b)                               #performing mathematical operation
print(a-b)                                   #both should be of same length
print(a*b)
print(a/b)

print(a.shape)
print(b.shape)
x=a.dot(b)
print("dot operation is ",x)

a10=np.array([1,2,3])
padd=np.pad(a10,pad_width=2,mode='constant')
print("padded array",padd)

transposed=np.transpose(a)              #to tansposed rows into columns
print(transposed)

c=np.array([[1,2,3],
            [4,6,3]])              #to concatenate two array
d=np.array([[6,67,7],
            [4,53,2]])

res=np.concatenate((c,d),axis=1)
print("concatenation is",res)


arr2=np.arange(9)
print(arr2)

result=np.split(arr2,3)
print(result)

e=np.array([[1,12,3],[2,4,5]])
f=np.resize(e,(3,2))
print(f)

print(np.append(e,[7,8,9]))
print("a:",np.append(e,[[7,8,9]],axis=0))

print(np.insert(e,3,[11,12]))

g=np.arange(12).reshape(3,4)        #to arrange 1 to 12 in 3x4 array
print(g)
h=np.delete(e,4)
print(h)

i=np.flip(e)
print(i)

k=np.flip(e,axis=0)
print(k)

j=np.sort(e)
print(j)

max_index=np.argmax(e)
print("max is ",max_index)








        
        
        