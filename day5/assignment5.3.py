import pandas as pd
#selecting rows based on condition
df = pd.DataFrame({
    'Name': ['Aman', 'sourabh', 'Chari', 'Dev'],
    'Age': [25, 30, 22, 35],
})
res=df[df['Age']>30]
print(res)

#selecting any row from a dataframe using iloc
print(df.iloc[0])
print(df.iloc[0:2])

#limited row selection with given column
print(df.iloc[0:2,0])
print(df.iloc[0:2,0:2])

#drop row from database
df2=pd.DataFrame({'A':[1,2,3,4,5],'B':[4,5,6,7,8],'C':[9,10,11,12,0]})
print(df2)
result4=df2[df2["C"]!=0]
print(result4)

#inserting
df.loc[len(df)]={'Name':'Rahul','Age':27}
print(df)

#list from rows
list=df.values.tolist()
print(list)