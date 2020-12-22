import pandas as pd
import numpy as np
# 读取最后一天的数据并设为np.int
last_day = 18
filename = './pandemicScrapy/data2020-12-'+str(last_day)+'.csv'
df = pd.read_csv(filename,encoding='utf-8')
df[['new', 'all', 'death', 'cure']] = df[['new', 'all', 'death', 'cure']].astype(np.int)
# 排序后输出前20，保存至csv
df.sort_values(by='all')
print(df.iloc[0:20,0:5])
print("Top 20 total:")
print(df.iloc[0:20,0:5]['all'].sum())
df.iloc[0:20,0:5].to_csv("./results/b-Top20-by-all.csv",index=None)
