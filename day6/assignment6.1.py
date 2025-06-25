import pandas as pd
df1=pd.DataFrame({
    'ID':[1,2,3],
    'Name':['Ram','Raju','Rehan'],
    'Age':[85,95,95]
})
df2=pd.DataFrame({
    'ID':[4,2,3],
    'Name':['Esha','Deepak','Dinesh'],
    'Age':[14,95,16]
})

#inner merge
result=df1.merge(df2,on='ID',how="inner")
print(result)

#left join
result2=df1.join(df2,rsuffix="_right",lsuffix="_left",how='left')
print(result2)

#right join
result3=df1.join(df2,rsuffix="_right",lsuffix="_left",how='right')
print(result3)

#right join using pd.merge()
result4=pd.merge(df1,df2,on='ID',how='right')
print("right\n",result4)

#join based on df.join()
result5=df2.join(df1,how='left',lsuffix='_df2', rsuffix='_df1')
print("join\n",result5)

#merge with multiple keys
result6=df1.merge(df2,on=['ID','Age'],how="inner")
print(result6)