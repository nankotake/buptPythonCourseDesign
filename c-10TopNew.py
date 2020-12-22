import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# 设置初始数据
first_day = 2
last_day = 18
# 读取所有数据并保存在新建的df中
df = pd.DataFrame()
for day in range(first_day, last_day + 1):
    filename = './pandemicScrapy/data2020-12-' + str(day) + '.csv'
    df_temp = pd.read_csv(filename, encoding='utf-8')
    df_temp.sort_values(by='country')
    if day == first_day:
        df = df_temp
    else:
        df['all'] = df_temp['all']
        df['new'] = df['new'] + df_temp['new']
        df['cure'] = df_temp['cure']
        df['death'] = df_temp['death']
# 按新增排序并输出至csv
df.sort_values(by='new')
df['new'] = df['new'].astype(np.int)
df.to_csv('./results/c-data2020-12-' + str(first_day) + 'to' + str(last_day)+'.csv', encoding='utf-8', index=False)
# 初始化plt
plt.style.use('seaborn-ticks')
plt.figure(facecolor='#EFF1FE')
plt.grid(True, linestyle='--')
plt.title("Top10-byNEW")
plt.rcParams['font.sans-serif'] = ['SimHei']
# 颜色序列
color_list = ['#60acfc', '#32d3eb', '#5bc49f', '#feb64d', '#ff7c7c',
              '#9287e7', '#60accf', '#927e87', '#5b4cf9', '#feb6d4']
# 获得并输出所有数据
for i in range(0, 10):
    temp_country = df['country'][i]
    temp_list = []
    temp_days = [i for i in range(first_day, last_day + 1)]
    for day in range(first_day, last_day + 1):
        filename = './pandemicScrapy/data2020-12-' + str(day) + '.csv'
        df_temp = pd.read_csv(filename, encoding='utf-8')
        temp_list.append(df_temp[df_temp['country'] == temp_country]['new'])
    plt.plot(temp_days, temp_list, color=color_list[i], linewidth=1.5, linestyle='-', label=temp_country)
    print(temp_country, ': \n', temp_list)
# 显示图例，表示图像
plt.legend([df['country'][i] for i in range(0, 10)], loc='best')
plt.show()
