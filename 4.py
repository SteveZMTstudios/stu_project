from dataclasses import dataclass
from ipaddress import collapse_addresses
import pandas as pd
data={'xm':['wjy','zjy','lcw'],'xb':['g','g','b'],'借阅次数':[28,56,37]}
df1=pd.DataFrame(data,columns=['xm','xb','借阅次数'])
print(df1[1:2])
