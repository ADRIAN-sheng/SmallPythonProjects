#爬虫 - 获得图片
import requests
from lxml import etree
#地址
url = 'http://www.netbian.com/mei/'
#发送请求 pip omsta;; requests

resp = requests.get(url,headers={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:126.0) Gecko/20100101 Firefox/126.0'})
resp.encoding = 'gbk' #结果的中文显示

#解析数据
xp = etree.HTML(resp.text)
img_urls = xp.xpath('//ul/li/a/@src')
img_names = xp.xpath('//ul/li/a/img/@alt')
#保存数据
for u,n in zip(img_urls,img_names):
    print(f'正在下载：图片名：{n}')
    #保存图片
    img_resp = requests.get(u,headers={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:126.0) Gecko/20100101 Firefox/126.0'})
    with open(f'./图片合成/img_f{n}.jpg','wb') as f:
        f.write(img_resp.content)
