import pandas as pd
import numpy as np
# 获取人口数据、最后一天的数据，并转为np.int
last_day = 18
df_population = pd.read_csv("./population/population.csv", encoding='utf-8', index_col=0)
df_population['population'] = df_population['population'].astype(np.int)
df_pandemic = pd.read_csv('./pandemicScrapy/data2020-12-' + str(last_day) + '.csv', encoding='utf-8', index_col=0)
df_pandemic['all'] = df_pandemic['all'].astype(np.int)
# 将人口数据归并到疫情数据中
df = pd.merge(df_pandemic, df_population, right_on='country', left_index=True, how='outer')
# 获取确诊率并排序
df['diagnosticRate'] = df['all'] / df['population'] * 100
df = df.sort_values(by='diagnosticRate',ascending=False)
# 输出前十名，前十名总确诊人数，并保存到csv
print(df.iloc[0:10,0:7])
print("diagnosticRate Top 10 total:")
print(df.iloc[0:10]['all'].sum())
df.iloc[0:10,0:7].to_csv('./results/d-diagnosticRateRank.csv', index=False)
