import pandas as pd
data={'xm':['a','b','c','d'],'xb':['f','m','f','m'],'ye':[6,2,3,10]}
df1=pd.DataFrame(data,columns=['xm','xb','ye'])
df2=df1.head(2)
df3=df1.tail(2)
a=df2['ye'].sum()
b=df3['ye'].sum()
print(b%a)
