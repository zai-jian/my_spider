from lxml import etree
from spider_res import request

url = "https://maoyan.com/board"
content = request(url)
with open('values/maoyanx.html', 'w', encoding='utf-8') as fp:
    fp.write(content)
tree = etree.HTML(content)
dl = tree.xpath('//dl[@class="board-wrapper"]')[0]
dd_list = dl.xpath('./dd')
for dd in dd_list:
    # 标题
    title = dd.xpath('./a/@title')
    # 详细页面
    detail_url = dd.xpath('./a/@href')
    url = 'https://maoyan.com'+ detail_url[0]
    # 演员
    action = dd.xpath('.//p[@class="star"]/text()')
    print(action[0].strip())



