import requests
from lxml import etree

#发送请求
url = 'https://nba.hupu.com/stats/players'
resp = requests.get(url,headers={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:126.0) Gecko/20111101 Firefox/126.0'})

#获取结果
e = etree.HTML(resp.text)
#解析结果
nos = e.xpath('//table[@class="player_table"]//tr/td[1]/text()')
names = e.xpath('//table[@class="player_table"]//tr/td[2]/a/text()')
teams = e.xpath('//table[@class="player_table"]//tr/td[3]/a/text()')
scores = e.xpath('//table[@class="player_table"]//tr/td[4]/text()')

#保存结果
with open('NBA_name.txt','w',encoding='utf-8') as f:
    for no,name,team,score in zip(nos,names,teams,scores):
        print(f'排名:{no} 姓名:{name} 球队:{team} 得分:{score}\n')
