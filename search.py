#pip install requests 发送请求模块
#pip install lxml 解释数据模块
#pip install Flask 模拟web服务模块
import requests
from lxml import etree
from flask import Flask,render_template

app = Flask(__name__) #创建一个支持web应用的对象

def get_mobile(phone):
    #发送请求的地址
    url = f'https://www.ip138.com/mobile.asp?mobile={phone}&action=mobile'
    #伪装自己
    headers = {'User-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:123.0) Gecko/20100101 Firefox/123.0'}
    #发送请求
    resp = requests.get(url,headers=headers)
    #设置中文显示
    resp.encoding = 'utf-8'
    #解析数据
    e = etree.HTML(resp.text)
    #编写xpath提取数据
    datas = e.xpath('//tr/td[2]/span/text()')

    #解析响应
    return datas

app.route('/')
def index():
    return render_template('index.html')

@app.route('/search_phone')
def search_phone():
    phone = requests.args.get('phone')
    data = get_mobile(phone)
    return '<br>'.join(data)

#get_mobile()
app.run(debug=True)