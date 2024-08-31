import requests

#audio_url = "https://aod.cos.tx.xmcdn.com/group39/M07/34/82/wKgJnlqChT2jRXU8AEn2S2TpSz0586.m4a"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"
}
url_list = 'https://www.ximalaya.com/revision/play/v1/show?id=67641798&sort=0&size=30&ptype=1'
#发送请求
url_list_resp = requests.get(url_list, headers=headers)
track_list = [(tack.get ('trackId'), tack.get('trackName')) for tack in url_list_resp.json().get('data').get('tracksAudioPlay')]

for id,name in track_list:
    #获取音频地址的链接
    audio_src = 'https://www.ximalaya.com/revision/play/v1/audio?id={id}&ptype=1'
    src = requests.get(audio_src, headers=headers)
    audio_url = src.json().get('data').get('src')
    response = requests.get(audio_url, headers=headers)
    #保存文件 w写文件 b字节流
    with open(f'audio/{name}.mp3', 'wb') as f:
        #resp.text返回的是网页的文本内容，resp.content返回的是二进制内容（图片、音频、视频等） resp.json()返回的是json数据
        f.write(response.content)

