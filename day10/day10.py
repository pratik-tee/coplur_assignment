import numpy as np
arr=np.array([1,2,3,4,5])

arr[0],arr[2]=arr[2],arr[0]               #for swapping of data
print(arr)


a2=np.array([[1,2,3,4],
             [13,14,15,16]])

a2[[0,1],:]=a2[[1,0],:]                  #for swapping 2d array
print("array is ",a2)

#a2[0,1],a2[1,0]=a2[1,0],a2[0,1]            #for swapping particular element in 2d array
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

result2=np.nan_to_num(a5,copy=True,nan=0.0,posinf=None,neginf=None)         # for replaing nan with particular values
print(result2)


a6=np.array([[10,20,30],[40,50,60]])
np.save('data1.npy',a6)

l=np.load('data1.npy')
print("The data is",l)

a7=np.array([70,80,90])
np.savez('data2.npz',arr1=a6,arr2=a7)

l2=np.load('data2.npz')
print(l2)

print('array 1 is ',l2['arr1'])
print('array 2 is ',l2['arr2'])

with open ('data3.txt','w') as f:
  f.write('1.0 2.0 3.0\n4.0 5.0 6.0\n7.0 8.0 9.0')
result4=np.loadtxt('data3.txt')                             #it convert numpy to array
print(result4) 

data4=np.array([[1,2,3],[4,5,6],[10,11,12]])
np.savetxt('output.txt',data4,delimiter=' ',fmt='%1.1f')       #delimiter is used for given space automatically

result5=np.loadtxt('output.txt')
print("the output file is \n",result5)

with open ('data4.csv','w') as f:
  f.write('1.0,2.0,3.0\n4.0,5.0,6.0\n7.0,8.0,9.0')
result6=np.genfromtxt('data4.csv',delimiter=',')
print("result is ",result6)



#algebra in numpy
arr1=np.array([[3,2],[1,2]])
arr2=np.array([5,5])
res3=np.linalg.solve(arr1,arr2)
print("solution of algebra is ",res3)

arr3=np.array([[3,-2,10],[1,2,11],[2,4,2]])             #3x+2y+10z=5
arr4=np.array([5,5,10])                                #1x+2y+10z=5
res4=np.linalg.solve(arr3,arr4)                        #2x+4y+2z=10
print("solution of algebra is ",res4)

arr5=np.array([[11,23],[32,54]])
arr6=np.array([89,80])

inv1=np.linalg.inv(arr5)
print(inv1)
result7=np.dot(inv1,arr6)
print(result7)

# matplotlib
import matplotlib.pyplot as plt
x=np.linspace(0,10,1000)
y=np.sin(x)


plt.plot(x,y,label='sin(x)',color='blue',linestyle='--')
plt.title("Line plot of sin(x)")
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()
plt.grid(True)
plt.show()

p=np.random.rand(50)
q=np.random.rand(50)
plt.scatter(p,q,color='green',alpha=0.7)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()

categories=['A','B','C','D']
values=[10,20,34,80]
plt.bar(categories,values,color='green')
plt.title("Bar graph")
plt.xlabel('categories')
plt.ylabel('values')
plt.show()



labels=['Python','C','C++','JAva']
sizes=[10,12,43,54]
plt.pie(sizes,labels=labels,autopct='%1.1f%%',startangle=140)
plt.title("pie chart")
plt.show()


































