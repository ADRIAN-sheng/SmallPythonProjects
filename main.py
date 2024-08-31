#发送请求
import requests
from lxml import etree

for i in range(1, 11):
    resp = requests.get('http://www.newhouse.fang.com/house/s/b9{i}/')
#解析数据
    resp.encoding = 'utf-8'

    e = etree.HTML(resp.text)
    names = [n.strip() for n in e.xpath('//div[@class="nlcd_name"]/a/text()')]
    addresses = e.xpath('//div[@class="address"]/a/@title')
    prices = [d.xpath('string(.)').strip() for d in e.xpath('//div[@class="nhouse_price"]')]
    comments = e.xpath('//span[@class="value_num"]/text()')
#处理数据
    data = []
    for n,a,p,c in zip(names,addresses,prices,comments):
        data.append([n,a,p,c])

#分析数据
import pandas as pd
df = pd.DataFrame(data,columns = ['小区名','地址','价格','评论数'])