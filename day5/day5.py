import pandas as pd
ds={
   'num':[3,5,7],
   'alpha':['A','B','C']
    }
df=pd.DataFrame(ds)
print(df)
print(type(df))

print(pd.__version__)

l=[4,7,9]
s=pd.Series(l,index=["X","Y","z"])
print(s)
print(s["Y"])

qmarks={"sub1":12,"sub2":45,"sub3":54}
m=pd.Series(qmarks,dtype=float)
print(m)

n=pd.Series(qmarks,index=["sub1","sub2"])
lst=n.tolist()                              #For convering data in list
print(lst)
print(type(lst))

data={
    "qmark":[3,4,5],"duration":[56,34,57]
}
df=pd.DataFrame(data)     
print(df)
print(df.loc[[0,2]])     #For printing values at particular location

result=df.columns
print(result)

df.columns=["Quiz","Time"]    # To change the name of the columns
print(df)



result2=df.iloc[0:3,0:3]
print("data",result2)


df2=pd.DataFrame([[1,2,3],[4,5,6],[7,8,9]],columns=['colA','colB','colC'])
print(df2)
col_A=df2.loc[0:3,'colA':'colB']
print(col_A)

df2.iloc[0:2,0]=[89,99]
print(df2)

result3=df2.drop(2)
print("after drop is ",result3)

df4=pd.DataFrame({'A':[1,2,3,4,5],'B':[4,5,6,7,8],'C':[9,10,11,12,0]},index=[101,102,103,103,104])
print(df4)
result4=df4[df4["C"]!=0]
print(result4)


df5=pd.DataFrame({'A':[1,2,3,4,5],'B':[4,5,6,7,8]})
print(df5)
result5=df5.drop(df5.index[2:4])
print(result5)


