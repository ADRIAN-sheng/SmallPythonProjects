from urllib.request import urlretrieve
import requests
from lxml import etree
from threading import Thread
from queue import Queue

def get_page():
    while not queue.empty():
        headers = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
        #获取一个url
        url = queue.get()
        resp = requests.get(url,headers=headers)


        #src = 'https://wx2.sinaimg.cn/bmiddle/0060lm7Tgy1g29772y10qj30u0140q4p.jpg'
        
        #获取数据
        e = etree.HTML(resp.text)

        src_list = e.xpath('//div[@class="tagbqpdiv"]/a/img/@src')
        name_list = e.xpath('//div[@class="tagbqpdiv"]/a/img/@title')

        for src,name in zip(src_list,name_list):
            #获取文件名后缀
            end = src.split('.')[-1]
            #拼接完整名字
            new_name = f'{name}.{end}'.replace('?','')
            print(f'正在下载{new_name}')
            urlretrieve(src, new_name)

if __name__ == '__main__':
    queue = Queue()
    for i in range(1,10):
        print(f'正在下载第{i}页图片')
        queue.put('https://www.fabiaoqing.com/biaoqing/lists/page/{i}.html')

    for j in range(3):
        #创建线程
        t = Thread(target = get_page)
        #并列线程
        t.start()
