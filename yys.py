#发送请求
#pip install requests
#pip install lxml
import requests
from lxml import etree
import os

url = 'https://api.yys.fun/api/wallpaper/random'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
list_resp = requests.get(url, headers=headers)
#print(resp.content)

#发送请求获取地址列表

#获取所有背景的地址
e=etree.HTML(list_resp.text)
imgs1=[url[:url.rindex('/')]+'/2732x2048.jpg' for url in e.xpath('//div[@class="tab-cont"][1]/div/div/img/@data-src')]
imgs2=[url[:url.rindex('/')]+'/2732x2048.jpg' for url in e.xpath('//div[@class="tab-cont"][2]/div/div/img/@data-src')]

if not os.path.exists('heng'):
    os.makedirs('heng')
if not os.path.exists('shu'):
    os.makedirs('shu')

for url in imgs1:
    resp = requests.get(url, headers=headers)
    file_name = url[url.rindex('20'):url.rindex('/')].replace('/','_')+'.jpg'
    print('正在下载：'+ file_name+'壁纸')
    with open(f'heng/{file_name}','wb')as f:
        f.write(resp.content)