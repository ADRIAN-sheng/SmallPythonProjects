#怎么发送请求
#pip install requests
#pip install lxml
import requests
from lxml import etree

#发送请求对象
url = 'https://dl.131437.xyz/book/douluodalu1/1.html'
while True:
        
    #套用user agent 伪装自己
    headers = {
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:123.0) Gecko/20100101 Firefox/123.0'
    }
    #发送请求
    resp = requests.get(url,headers=headers)
    #设置编码
    resp.encoding = 'utf-8'
    #响应信息
    #print(resp.text)

    e = etree.HTML(resp.text)
    info = '\n'.join(e.xpath('//div[@class="m=post"]/p/text()'))
    title = e.xpath('//h1/text()')[0]
    url = f'https://dl.131437.xyz{e.xpath("//tr/td[2]/a/@href")[0]}'
    #print(info)
    #print(title)
    #print(url)

    #保存内容
    #如果是单次输入 使用‘w'，多次重复打开文档使用'a'，'w'会清空上次输入内容
    with open('斗罗大陆.text','a',encoding='utf-8') as f:
        f.write(title+'\n\n'+info+'\n\n')

    #判断是否为最后一页
    if url == '/book/douluodalu1/':
        break
    else:
        continue