#发送请求
#pip install requests
#pip install lxml
import requests
from lxml import etree

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36' 
}
resp = requests.get('https://www.qb5.tw/top/allvisit/',headers=headers)

#接受响应
e = etree.HTML(resp.text)
types = e.xpath('//div[@id="articlelist"]/ul[2]/li/span[1]/text()')
names = e.xpathe('//div[@id="articlelist"]/ul[2]/li/span[2]/a/text()')
authors = e.xpath('//div[@id="articlelist"]/ul[2]/li/span[3]/text()')
counts = e.xpath('//div[@id="articlelist"]/ul[2]/li/span[5]/text()')
nums = e.xpath('//div[@id="articlelist"]/ul[2]/li/span[6]/text()')
#分析
datas = []
for t,name,author,count,num in zip(types,names,authors,counts,nums):
    #print(f'{t}--{name}--{author}--{count}--{num}')
    datas.append([t,name,author,count[:-1],num])

#pip install pandas
pip install matplotlib
import pandas as pd
import matplotlib
df = pd.DataFrame(datas,columns=['类型','名称','作者','字数','推荐'])

#数据分析
df.describe()
#按类型统计
df.groupby('类型').count()
df.类型.hist() #直方图
sorted([f.name for f in matplotlib.font_manager.fontManager.ttflist])
#按推荐数排序
df['推荐'] = df['推荐'].astype(int)
df[df.类型=='玄幻'].sort_values(by='推荐',ascending=False)