import pandas as pd
import matplotlib.pyplot as plt

# 初始化数据
last_day = 18
filename = './pandemicScrapy/data2020-12-' + str(last_day) + '.csv'
# 读取最后一天的疫情数据
df = pd.read_csv(filename, encoding='utf-8')
# 按累计确诊人数排序
df = df.sort_values(by='all', ascending=False)
# 按1，2-3，4-8，9-16，17-185分列数据
labelList = []
labelTemp = []
labelTemp.append(df.iloc[0:1, 0:1].values.tolist())
labelTemp.append(df.iloc[1:3, 0:1].values.tolist())
labelTemp.append(df.iloc[3:9, 0:1].values.tolist())
labelTemp.append(df.iloc[9:17, 0:1].values.tolist())
labelTemp.append(df.iloc[17:186, 0:1].values.tolist())
numList = []
numList.append(df.iloc[0:1, 2:3].values.sum())
numList.append(df.iloc[1:3, 2:3].values.sum())
numList.append(df.iloc[3:9, 2:3].values.sum())
numList.append(df.iloc[9:17, 2:3].values.sum())
numList.append(df.iloc[17:33, 2:3].values.sum())
# 合并国家名（如印度+巴西）
tempint = 0
for i in range(0, 5):
    if len(labelTemp[i]) < 4:
        tempstr = ''
        tempint += len(labelTemp[i])
        for j in range(len(labelTemp[i])):
            tempstr = tempstr + labelTemp[i][j][0] + ' '
    else:
        tempstr = '其他 ' + str(tempint)
        tempint += len(labelTemp[i])
        tempstr += ' - ' + str(tempint)
    labelList.append(tempstr)
# 初始化plt
plt.style.use('seaborn-ticks')
plt.figure(facecolor='#EFF1FE')
plt.title('Pie Graph of Pandemic at 2020-12-' + str(last_day))
plt.rcParams['font.sans-serif'] = ['SimHei']
# 颜色表
colors = ['#60acfc', '#32d3eb', '#5bc49f', '#feb64d', '#ff7c7c', '#9287e7']
# 生成饼图
patches, texts, autotexts = plt.pie(numList, labels=labelList, labeldistance=1.2, autopct='%1.1f%%',pctdistance=0.8, colors=colors)
# 显示
plt.show()
