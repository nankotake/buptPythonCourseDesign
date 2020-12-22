import numpy as np
import pandas as pd
# 初始化数据
last_day = 18
# 读取人口、疫情数据
df_population = pd.read_csv("./population/population.csv", encoding='utf-8', index_col=0)
df_population['population'] = df_population['population'].astype(np.int)
df_pandemic = pd.read_csv('./pandemicScrapy/data2020-12-' + str(last_day) + '.csv', encoding='utf-8', index_col=0)
df_pandemic['all'] = df_pandemic['all'].astype(np.int)
# 归并两组数据
df = pd.merge(df_pandemic, df_population, right_on='country', left_index=True, how='outer')
# 获取确诊、死亡率
df['diagnosticRate'] = df['all'] / df['population'] * 100
df['deathRate'] = df['death'] / df['all'] * 100
# 去除空数据
df['diagnosticRate'] = df['diagnosticRate'].dropna()
df['population'] = df['population'].dropna()
# 排序
df = df.sort_values(by='population',ascending=True)
df = df.sort_values(by='diagnosticRate',ascending=False)
df = df.sort_values(by='deathRate',ascending=True)
# 显示前十组数据，并保存全部到csv
print(df.iloc[0:10,0:8])
df.to_csv('./results/3-getbest.csv',encoding='utf-8')
