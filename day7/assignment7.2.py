import pandas as pd
print(pd.date_range('6/1/2025',periods=5))

#convert a column or string into a datetime object
df=pd.DataFrame({'date_str':['2025-06-27','2025-06-28']})
df['date']=pd.to_datetime(df['date_str'])
print(df)


#filtering of date range 
result=df[df['date']>'2025-06-27']
print(result)


