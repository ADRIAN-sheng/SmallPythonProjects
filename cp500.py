#发送请求
import requests
from lxml import etree
#获取结果
url = 'https://datachart.500.com/ssq'
headers={
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
    'Referer':'https://www1.rmfysszc.gov.cn/'
}
resp = requests.get(url,headers=headers)

resp.encoding = 'gbk'
#解析结果
e = etree.HTML(resp.text)
reds = [tr.xpath('./td[contains(@class,"chartBall01")]/text()') for tr in e.xpath('//tbody[@id='tdata']/tr[not(contains(@class,"tdbck"))]')]
blues =  e.xpath('//tbody[@id="tdata"]/tr[not(contains(@class,"tdbck"))]/td[contains(@class,"chartBall02")]/text()')

for r,b in zip(reds,blues):
    print(f'红球是：{r}，蓝球是：{b}')