import pandas as pd

#pandas dataframe with a two dimensional python list
data=[[1,2,3],[4,5,6],[7,8,9]]
df=pd.DataFrame(data,columns=['A','B','C'])
print(df)

#dataframe from python dist
data2={'Name':['Ram','Shyam','Ghanshyam'],'Address':['jaipur','jodhpur','jagatpure'],'Age':[9,10,11]}
df2=pd.DataFrame(data2)
print(df2)

#dataframe using list of list
data3=[
    ['A',1],['B',2],['C',3]
] 
df3=pd.DataFrame(data3)
print(df3)

#dataframe using lsit of tuples
tup=[(1,'Ram'),(2,'ghanshyam'),(3,'shyam')]
df4=pd.DataFrame(tup)
print(df4)

#dataframe using list of dict
data5=[{'Name':'ramu'},{'Name':'tilu'},{'Name':'baba'}]
df5=pd.DataFrame(data5)
print(df5)