import pandas as pd           #pandas are used as data analysis ,working with tables,reading and writing of csv files(grouping,sorting,filtering)
import numpy as np           #numpy library is used for numerical operations in python
data={"Col1":[3,np.nan,np.nan,2],
      "Col2":[1.0,pd.NA,pd.NA,2.0]}
df=pd.DataFrame(data)
print(df)

#filling na values with '-'
f=df.fillna('-')
print(f)

df2=pd.DataFrame([[6,7,6],[4,4,3],[2,2,9]],
                 index=['a','b','d'],
                 columns=['one','two','three'])
print(df2)
df2=df2.reindex(['a','c','d','e','f'])
print(df2)

#Forward filling
result=df2.ffill()
print('After forward filling \n',result)

#Backward filling
result2=df2.bfill()
print("After backward filling\n",result2)


# here we apply limit on forward filling
result3=df2.ffill(limit=1)               
print("After backward filling\n",result3)


#here we replace the values 
df3=pd.DataFrame({'one':[4,5,6,1],'two':[8,9,5,6],'three':[1,7,3,2]})  
print("Only printing temporary value:\n",df3.replace({5:500,6:600,7:700}))            #it only prints the temporary changed value
df3=df3.replace({5:500,6:600,7:800})                #it get permanently replaced
print("after replacing permanently:\n",df3)


df4=pd.DataFrame(['Rs4000','Rs45678 condition attched'],columns=['P'])
print(df4)

#df4['P']=df4['P'].str.replace(r'\D+','',regex=True).astype('int')
df4['Q']=df4['P'].str.replace(r'\D+','',regex=True).astype('int')
print("after replacing:\n",df4)


data={'alpha':['A','B','V','B','V'],
      'num':[1,2,3,4,5]}
df5=pd.DataFrame(data)
group_data=df5.groupby('alpha')['num'].sum()   
print(group_data)

group_data2=df5.groupby('alpha')['num'].max()   #it gives the maximum among the same column
print(group_data2)

group_data3=df5.groupby('alpha')['num'].agg([sum,max])
print(group_data3)

data2={'alpha':['A','B','V','B','V'],
       'subalpha':['Q','W','E','R','T'],
      'num':[1,2,3,4,5]}    
df6=pd.DataFrame(data2)
group_data3=df6.groupby(['alpha','subalpha'])['num'].mean()
print(group_data3)


#sorting of data
data3={
    'Name':['x','y','z'],
    'Age':[27,56,14]
}
df7=pd.DataFrame(data3)
result4=df7.sort_values(by='Age',ascending=False)      #by default ascending but for descending use ascending=False
print(result4)

data4={
    'Name':['x','y','z','x'],
    'Score':[273,563,143,456]
}
df8=pd.DataFrame(data4)
result5=df8.sort_values(by=['Name','Score'],ascending=[True,False])
print(result5)


data5={
    'Name':['p','q','r'],
    'Age':[270,560,140]
}
df9=pd.DataFrame(data5)
df9.sort_values(by='Age',inplace=True)          #inplace is used when we dont want to create new dataframe
print(df9)

result6=df9.sort_index(ascending=False)             #for sorting the index 
print(result6)

result7=df9.sort_index(axis=1)                   #IT SORTS THE COLUMNS NOT ROWS
print(result7)

print(pd.date_range('6/1/2025',periods=5))


#csv file
df10=pd.read_csv('customers.csv')
print(df10.to_string())

print(df10.head(5))

print(df10.info())
print(df10.describe())

print(df10.shape)
print(df10.columns)

print(df10['Period'])

filter_df=df10[df10['Period']>2015]
print(filter_df)

group_data=df10.groupby('Data_value')['Period'].mean()
print(group_data)

print(df10["Period"].value_counts())

pd.options.display.max_rows=100
df11=pd.read_csv('customers.csv')
print(df11)

new_df=df.dropna()
print("After droping\n",new_df)

df=pd.read_csv('customers.csv')
x=df['Period'].mean()
df.fillna({'Period':x},inplace=True)
print(df)

df=pd.read_csv('customers.csv')
x=df['Period'].median()
df.fillna({'Period':x},inplace=True)
print(df)


