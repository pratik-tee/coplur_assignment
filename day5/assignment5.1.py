import pandas as pd
dict={'A':10,'B':20,'C':30}
series=pd.Series(dict)
print(dict)

list=[10,20,200]
df=pd.Series(list)
print(df)

print(df[2])
print(df.loc[[0,2]])

result=df.iloc[0:2]
print("data",result)
