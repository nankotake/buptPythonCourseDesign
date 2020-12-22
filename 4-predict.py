import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
# 初始化数据
first_day = 2
selected_day = 11
last_day = 18
# 初始化plt
plt.style.use('seaborn-ticks')
plt.rcParams['font.sans-serif'] = ['SimHei']
fig, ax = plt.subplots(2, 2)
# 获取收集到的全部数据并转为np.int
df_collect = pd.DataFrame(columns=['day', 'new', 'all', 'death', 'cure'])
df_last = pd.DataFrame(columns=['day', 'new', 'all', 'death', 'cure'])
for day in range(first_day, last_day + 1):
    filename = './pandemicScrapy/data2020-12-' + str(day) + '.csv'
    df = pd.read_csv(filename, encoding='utf-8')
    df[['new', 'all', 'death', 'cure']] = df[['new', 'all', 'death', 'cure']].astype(np.int)
    if day <= selected_day:
        df_collect.loc[day - first_day] = [day, df['new'].sum(), df['all'].sum(), df['death'].sum(), df['cure'].sum()]
    df_last.loc[day - first_day] = [day, df['new'].sum(), df['all'].sum(), df['death'].sum(), df['cure'].sum()]
df_collect[['day', 'new', 'all', 'death', 'cure']] = df_collect[['day', 'new', 'all', 'death', 'cure']].astype(np.int)
df_last[['day', 'new', 'all', 'death', 'cure']] = df_last[['day', 'new', 'all', 'death', 'cure']].astype(np.int)
# 获取日期等数据的列表
days = df_collect['day'].values.tolist()
alls = df_collect['all'].values.tolist()
news = df_collect['new'].values.tolist()
deaths = df_collect['death'].values.tolist()
cures = df_collect['cure'].values.tolist()
# 生成二阶线性回归拟合预测模型
allModel2 = np.polyfit(days,alls,2)
newModel2 = np.polyfit(days,news,2)
deathModel2 = np.polyfit(days,deaths,2)
cureModel2 = np.polyfit(days,cures,2)
# 清空以用来存放预测数据
alls.clear()
news.clear()
deaths.clear()
cures.clear()
# 生成预测数据
for i in range(first_day,last_day+1):
    all_now = np.polyval(allModel2,i)
    new_now = np.polyval(newModel2,i)
    death_now = np.polyval(deathModel2,i)
    cure_now = np.polyval(cureModel2,i)
    alls.append(all_now)
    news.append(new_now)
    deaths.append(death_now)
    cures.append(cure_now)
# 为日期添加采样之后的数据
for i in range(selected_day+1,last_day+1):
    days.append(i)
# 生成四个图表显示预测数据与真实数据
ax[0][0].plot(days,alls,color='r',label='origin')
ax[0][0].plot(days,df_last['all'].values.tolist(),color='b',label='predicted')
ax[0][1].plot(days,news,color='r',label='origin')
ax[0][1].plot(days,df_last['new'].values.tolist(),color='b',label='predicted')
ax[1][0].plot(days,deaths,color='r',label='origin')
ax[1][0].plot(days,df_last['death'].values.tolist(),color='b',label='predicted')
ax[1][1].plot(days,cures,color='r',label='origin')
ax[1][1].plot(days,df_last['cure'].values.tolist(),color='b',label='predicted')
# 为四个图表确认格式
titles = ['all','new','death','cure']
for i in range(0,2):
    for j in range(0,2):
        ax[i][j].ticklabel_format(style='plain')
        ax[i][j].set_title(titles[i*2+j])
        ax[i][j].legend(['predicted','origin'],loc='best')
# 显示
plt.show()
