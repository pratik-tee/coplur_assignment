import pandas as pd 
df=pd.read_csv('employees.csv')
print(df)


print(df.head())

print(df.info())
print(df.describe())

print(df['Salary'])

print(df.shape)

group_data=df.groupby('First Name')['Salary'].mean()
print(group_data)


new_df=df.dropna()
print("After droping\n",new_df)

df=pd.read_csv('employees.csv')
x=df['Salary'].mean()
df.fillna({'Salary':x},inplace=True)
print(df)


print(df["Salary"].value_counts())