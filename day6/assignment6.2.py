import pandas as pd
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

three=pd.DataFrame({
    'Name':['C1','C2','C3','C4'],
    'Subject':['sub5','sub6','sub3','sub8'],
    'Marks':[78,73,10,75]},
                 index=[1,6,3,4])
#concatenate two of them
result=pd.concat([one,two],ignore_index=True)
print(result)

#merge with third
result2=pd.merge(result,three,on='Subject',how='inner')
print('merge\n',result2)






