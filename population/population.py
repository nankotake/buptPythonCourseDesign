# 导入相关函数包
import requests
from bs4 import BeautifulSoup
import pandas as pd

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
}#爬虫[Requests设置请求头Headers],伪造浏览器
listData=[]   #定义数组
counData=[]   #定义数组
for i in range(1,10):
    if i==1:
        url= 'https://www.phb123.com/city/renkou/rk.html'
    else:
        url = 'https://www.phb123.com/city/renkou/rk_%s.html'%i
    params = {"show_ram":1}
    response = requests.get(url,params=params, headers=headers)    #访问url
    soup = BeautifulSoup(response.text, 'html.parser')             #获取网页源代码
    tr = soup.find('table',class_='rank-table').find_all('tr')     #.find定位到所需数据位置  .find_all查找所有的tr（表格）
    # 去除标签栏
    for j in tr[1:]:        #tr[1:]遍历第1列到最后一列，表头为第0列
        td = j.find_all('td')#td表格
        country = td[1].get_text().strip()        #国家
        counData.append(country)
        number = td[2].get_text().strip()         #人口数量
        number = number.replace(',','')
        num = int(number)
        listData.append([country,num])

# 存储结果
dataRank = pd.DataFrame(listData,columns=["country","population"])
dataRank.to_csv("population.csv",index=False)
