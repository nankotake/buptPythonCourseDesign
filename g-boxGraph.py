import pandas as pd
import matplotlib.pyplot as plt
# 初始化数据
last_day = 18
filename = './pandemicScrapy/data2020-12-' + str(last_day) + '.csv'
# 读取最后一天的疫情数据
df = pd.read_csv(filename, encoding='utf-8')
df = df.sort_values(by='all', ascending=False)
# 生成箱型图
ax = df.boxplot(column=['all'],meanline=True,showmeans=True,vert=True)
# 在图中分别表示平均值、中位值、上四分位数、下四分位数
ax.text(1.1,df['all'].mean(),df['all'].mean())
ax.text(1.1,df['all'].median(),df['all'].median())
ax.text(0.9,df['all'].quantile(0.25),df['all'].quantile(0.25))
ax.text(0.9,df['all'].quantile(0.75),df['all'].quantile(0.75))
# 显示
plt.show()
