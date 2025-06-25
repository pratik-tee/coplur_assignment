import pandas as pd
#airthemetic operations on dataframe
d2={
    'Id':[1,2],
     'age':[26,27]
    }
df=pd.DataFrame(d2)
print(df)

print('addition is\n ',df+2)

print('subtraction is\n ',df-2)

print('multiplication is\n ',df*2)

print('Division is\n ',df//2)

print('modulo is\n ',df%2)

df['C']=df['Id']+df['age']
print(df)

df1=pd.DataFrame({'A':[1,2,3],'B':[4,5,6]})
df2=pd.DataFrame({'A':[10,20,30],'B':[40,50,60]},index=[1,2,3])    #addition is perform according to indexing 
print(df1)
print(df2)
print("addition is \n",df1+df2)
print('subtraction is\n ',df1-df2)

print('multiplication is\n ',df1*df2)

print('Division is\n ',df1//df2)

print('modulo is\n ',df1%df2)


#dataframe concatenation
one=pd.DataFrame({
    'Name':['A1','A2','A3','A4'],
    'Subject':['sub1','sub2','sub3','sub4'],
    'Marks':[98,99,100,95]},
                 index=[1,2,3,4])
two=pd.DataFrame({
    'Name':['B1','B2','B3','B4'],
    'Subject':['sub5','sub6','sub3','sub4'],
    'Marks':[88,83,100,85]},
                 index=[1,2,3,4])
result=pd.concat([one,two],keys=['a','b'],ignore_index=True)
print(result)
result2=pd.concat([one,two],axis=1)
print(result2)

left=pd.DataFrame({
    'id':[1,2,3,4],
    'Name':['A1','A2','A3','A4'],
    'Subject':['sub1','sub2','sub3','sub4'],
    'Marks':[98,99,100,95]},
                 )
right=pd.DataFrame({
    'id':[1,2,3,5],
    'Name':['B1','B2','B3','B4'],
    'Subject':['sub5','sub6','sub3','sub4'],
    'Marks':[88,83,100,85]},
                )
 
result3=left.merge(right,on='id')
print(result3)
 
result4=left.merge(right,on=['id','Subject'])
print(result4)

#'how' method is used  
result5=left.merge(right,on='Subject',how="left")
print(result5)

result6=left.merge(right,on='Subject',how="right")     
print(result6)

result7=left.merge(right,on='Subject',how="outer")     #take all the values on both side 
print(result7)

result8=left.merge(right,on='Subject',how="inner")    #only take common values like intersection
print(result8)

#join
result9=left.join(right,rsuffix="_right",lsuffix="_left")
print(result9)

#pivoting            To rearrange the data
df=pd.DataFrame({"Col1":range(12),"Col2":["A","A","A","B","B","B","C","C","C","D","D","D"],
"date":pd.to_datetime(["2025-06-20","2025-06-21","2025-06-22"]*4)})
print(df)

pivoted=df.pivot(index="date",columns="Col2",values="Col1")          #in this line data is formated
print(pivoted)


data={
    'Course':['cs','civil','mech','cs','civil'],
    'year':[1,2,3,1,2],
    'student':[100,120,456,752,962]
    }
df5=pd.DataFrame(data) 
print("original data",df5)

pivot_df=df5.pivot_table(                 
    values='student',
    index='Course',
    columns='year',
    aggfunc='sum'
)
print(pivot_df)