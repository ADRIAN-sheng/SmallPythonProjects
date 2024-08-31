#pip install pandas
import pandas as pd

#读入文件
data = pd.read_excel('data.xlsx')
#拆分列表内容
data['Year'] = data['type'].apply(lambda x:x.split('/')[0].strip())
data['Country'] = data['type'].apply(lambda x:x.split('/')[1].strip())
data['Type'] = data['type'].apply(lambda x:x.split('/')[2].strip())

##导出到Excel##
writer = pd.ExcelWriter('temp.xlsx')
#data.to_excel(writer,sheet_name='原始数据')

#pandas 的一些用法
#print(data[data['Country']=='美国'])
#print(data['Year'].unique())

"""""
#按年输出
for i in data['Year'].unique():
    data[data['Year'] == i].to_excel(writer,sheet_name=i)
"""""

#根据type 分
#print(data[data['Type'].str.contains('科幻')])
type_list = set(z for i in data['Type'] for z in i.split(' '))
"""
type_list = []
for i in data['Type']:
    for z in i.split(' ')
        type_list.append(z)
set(type_list)
"""
#type_list.remove('1987(中国大陆)‘)

for ty in type_list:
    data[data['Type'].str.contains(ty)].to_excel(writer,sheet_name=ty)

writer.close()    