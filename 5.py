import pandas as pd
data={'xm':['1','2','3','4'],'xb':['nv','nv','nan','nan'],'借阅次数':[18,16,30,26]}
df1=pd.DataFrame(data,columns=['xm','xb','借阅次数'])
a=df1['借阅次数'].max()
b=df1.借阅次数.min()
print(a+b)


