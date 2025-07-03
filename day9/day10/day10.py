import numpy as np
arr=np.array([1,2,3,4,5])

arr[0],arr[2]=arr[2],arr[0]               #for swapping of data
print(arr)


a2=np.array([[1,2,3,4],
             [13,14,15,16]])

#a2[[0,1],:]=a2[[1,0],:]                  #for swapping 2d array
print("array is ",a2)

a2[0,1],a2[1,0]=a2[1,0],a2[0,1]            #for swapping particular element in 2d array
print(a2)

a3=np.array([[1,2,3,4],
             [13,14,15,16],
             [7,2,6,8]])
a3[:,[0,1,2]]=a3[:,[1,2,0]]  
print(a3)

a4=np.array([[[1,2,3],
              [4,5,6]],                  #for swapping particular element in 3d array
            [[9,8,7],
             [5,2,7]]])
a4[:,:,[0,2]]=a4[:,:,[2,0]]

print(a4)

a5=np.array([1,2,np.nan,4])
res=np.isnan(a5)                        #to check the value is nan or not
print(a5)
print(res)

#result=a5[~np.isnan(a5)]               # for removing nan value
print(a5)
#print(result)

result2=np.nan_to_num(a5,copy=True,nan=0.1,posinf=None,neginf=None)         # for replaing nan with particular values
print(result2)
































