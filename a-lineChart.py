import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# 设置初始数据
first_day = 2
last_day = 18
fig, ax = plt.subplots(5,1)
new = []
all = []
cure = []
death = []
now = []
days = []
# 读取所有获得的数据
for day in range(first_day, last_day + 1):
    filename = './pandemicScrapy/data2020-12-' + str(day) + '.csv'
    df = pd.read_csv(filename, encoding='utf-8')
    df[['new', 'all', 'death', 'cure']] = df[['new', 'all', 'death', 'cure']].astype(np.int)
    new.append(df['new'].sum())
    all.append(df['all'].sum())
    cure.append(df['cure'].sum())
    death.append(df['death'].sum())
    now.append(df['all'].sum() - df['cure'].sum() - df['death'].sum())
    days.append(day)
# 作图
ax[0].plot(days, new, color='#60acfc', linestyle='-', label='new')
ax[1].plot(days, all, color='#32d3eb', linestyle='-', label='all')
ax[2].plot(days, cure, color='#5bc49f', linestyle='-', label='cure')
ax[3].plot(days, death, color='#feb64d', linestyle='-', label='death')
ax[4].plot(days, now, color='#ff7c7c', linestyle='-', label='now')
# 设置坐标方式
ax[0].ticklabel_format(style='plain')
ax[1].ticklabel_format(style='plain')
ax[2].ticklabel_format(style='plain')
ax[3].ticklabel_format(style='plain')
ax[4].ticklabel_format(style='plain')
# 设置标题
ax[0].set_title('New')
ax[1].set_title('All')
ax[2].set_title('Cure')
ax[3].set_title('Death')
ax[4].set_title('Now')
# 在图上标出数字
for a,b in zip(days,new):
    ax[0].text(a,b,'%d'%b,ha='center',va='center_baseline')
for a,b in zip(days,all):
    ax[1].text(a,b,'%d'%b,ha='center',va='center_baseline')
for a,b in zip(days,cure):
    ax[2].text(a,b,'%d'%b,ha='center',va='center_baseline')
for a,b in zip(days,death):
    ax[3].text(a,b,'%d'%b,ha='center',va='center_baseline')
for a,b in zip(days,now):
    ax[4].text(a,b,'%d'%b,ha='center',va='center_baseline')
# 显示图例
fig.legend(['new','all','cure','death','now'])
# 显示图像
plt.show()
