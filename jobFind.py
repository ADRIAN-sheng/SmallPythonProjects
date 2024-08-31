import requests
#自动获取cookie
index_url = 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput='
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:126.0) Gecko/20100101 Firefox/126.0'}
resp = requests.get(index_url, headers=headers)

with open('Jobs.csv', 'w', encoding='utf-8') as f:

    list_url = 'https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false'

    for i in range(1, 10):
        data = {
            'first':'true',
            'pn': i,
            'kd':'python'
        }
        print(f'正在爬取第{i}页...')
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:126.0) Gecko/20100101 Firefox/126.0',
            'origin': 'https://www.lagou.com',
            'Referer': 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput='
        }
    #发送请求
        list_response = requests.post(list_url, data=data,headers=headers,cookies=resp.cookies)
    #获取showID 为了获取后面的数据
        show_id = list_response.json()['content']['showId']
        data['first'] = 'false'
        data['sid'] = show_id
    #服务器响应
        for w in list_response.json()['content']['positionResult']['result']:
            f.write(f'{w.get("positionName")},{w.get("companyFullName")},{w.get("education")},{w.get("salary")}\n')
