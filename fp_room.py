#发送请求
#pip install requests
#pip install lxml
import requests
from lxml import etree

form_data={
    'type':'1', 'name':'', 'area':'北京市', 'city': '北京市', 'city1':'==请选择==', 'city2':'==请选择==', 'state': '0', 'time':'0',
    'time1':'', 'time2':'', 'money':'', 'money1':'', 'number' :'0', 'fid1':'','fid2':'','fid3':'', 'order' :'0', 'page':'1',
    'include': 'O'
}

headers={
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
    'Referer':'https://www1.rmfysszc.gov.cn/'
}

resp = requests.post('https://www.rmfysszc.gov.cn/projectHandle.shtml',data=form_data, headers=headers)


#查看结果

e = etree.HTML(resp.text)
#提取数据
#标题
title = e.xpath( '//div[@class="product"]/div[@class="p_img"]/a/@title')
#数据类型
infos = e.xpath('//div[@class="product"]/div[2]/p[1]/text()')
#价格1
price1 = e.xpath( '//div[@class="product"]/div[2]/p[1]/span/text()')
#价格2
price2 = e.xpath( '//div[@class="product"]/div[2]/p[2]/span/text()')

#处理数据
for t,i,p1,p2 in zip(title,infos,price1,price2):
    if i=='起拍价':
        tp=p2
    else:
        tp=p1
    print(f'名称：{t} -------- 评估价：{tp}')