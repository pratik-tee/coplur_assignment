import numpy as np
# Q1 Replace Nan with 0 and Interchange 3 rows and 3 columns of 2D array
[[6, -8, 73, -110], [np.nan, -8, 0, 94]]
a=np.array([[6,-8,73,-110],[np.nan,-8,0,94]])
result=np.nan_to_num(a,copy=True,nan=0.0)       
print(result)

reshaped=a.reshape(4,2)
print(reshaped)

#Q2.Move axes of 3D array to new positions

a2=np.array([[[21,42,83],
              [24,35,26]],                 
            [[94,8,7],
             [5,2,7]]])
a2[:,:,[0,2]]=a2[:,:,[2,0]]
print(a2)


#Q3 Replace NaN values with average of columns

col_mean=np.nanmean(a,axis=0)
result2=np.nan_to_num(a,copy=True,nan=col_mean) 
print(result2)



#  create a NumPy 1d-arrays
arr1 = np.array([3, 4])
arr2 = np.array([1, 0])

print(arr1)
print(arr2)

avg = (arr1 + arr2) / 2
print("Average of NumPy arrays:\n", avg)


#Calculate average mean median mode values of two NumPy 2d-arrays
arr3=np.array([[1, 2, 3],
                 [4, 5, 6]])

arr4=np.array([[6, 5, 4],
                 [3, 2, 1]])

combined=np.concatenate((arr3, arr4))

average = np.mean(combined)
print(average)

median = np.median(combined)
print(f"Median: {median}")

#mode=np.mod(combined)
#print(mode)


# Q8 Solve the following equation using linalg() and inverse Matrix method:
# x - 2y + 3z = 9
# -x + 3y - z = -6
# 2x - 5y + 5z = 17


arr1=np.array([[1,-2,3],[-1,3,-1],[2,-5,5]])
arr2=np.array([9,-6,17])
res3=np.linalg.solve(arr1,arr2)
print("solution of algebra is ",res3)

# Q9 Using "Customizing Matplotlib Visualizations" discussed in NumPy session4 notes plot graph to compare your at least 2 semester result
import matplotlib.pyplot as plt

subjects = ['Math', 'Physics', 'Chemistry', 'English']
sem1=[85, 78, 92, 74]
sem2=[88, 82, 89, 80]


plt.plot( sem1, label='Semester 1', color='blue', linestyle='--')
plt.plot( sem2, label='Semester 2', color='red', linestyle='--')

plt.title("Comparison of Semester 1 and Semester 2 Results")
plt.xlabel('Subjects')
plt.ylabel('Marks')
plt.legend()
plt.grid(True)
plt.show()

























