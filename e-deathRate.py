import pandas as pd
# 初始化数据
last_day = 18
select_range = 10
# 读取最后一天的疫情数据并算出死亡率
df = pd.read_csv('./pandemicScrapy/data2020-12-' + str(last_day) + '.csv', encoding='utf-8', index_col=0)
df['deathRate'] = df['death'] / df['all']
# 按死亡率排序
df = df.sort_values(by='deathRate')
# 选择前select_range个数据输出并保存至csv
print(df.iloc[0:select_range,0:5])
print("deathRate Bottom 10 total:")
print(df.iloc[0:select_range]['all'].sum())
df.iloc[0:select_range,0:5].to_csv('./results/e-deathRateRank.csv')
