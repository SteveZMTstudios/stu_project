import pandas as pd
data={'xm':['a','b','c','d'],'xb':['m','f','m','m'],'ye':[6,1,3,10]}
df1=pd.DataFrame(data,columns=['xm','xb','ye'])
a=df1['ye'].mean()
b=df1.xm.count()
print(a,b)
