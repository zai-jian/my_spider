import json
import random
import re

import requests

url = "http://guba.eastmoney.com/"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
             AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134",}
proxies = [{'http':'120.78.94.212:8866'},
            {'https':'27.152.91.157:9999'},
            {'http':'111.29.3.220:8080'},
            {'https':'113.124.92.35:9999'},
            {'http':'111.29.3.195:80'},
           ]
proxy = random.choice(proxies)
print(proxy)
content = requests.get(url=url, headers=headers, proxies=proxy).content.decode('utf-8')
ul_re = re.compile(r'<ul class="newlist" tracker-eventcode="gb_xgbsy_ lbqy_rmlbdj">[\d\D]*?</ul>')
ul = ul_re.findall(content)[0]
with open('guba.html', 'w', encoding='utf-8') as  fp:
    fp.write(ul)
li_re = re.compile(r'<li>\r\n([\d\D]*?</li>)')
li = li_re.findall(ul)

gu_list = []
for values in li:
    gu_dict = {}
    # 阅读数和评论数
    nums_re = re.compile(r'<cite>\s+(\d*?)\s+</cite>')
    nums = nums_re.findall(values)
    gu_dict['read_nums'] = nums[0]
    gu_dict['comment_nums'] = nums[1]
    # 详细页面地址和标题
    detail_re = re.compile(r'</em>\s+<a href="([\d\D]*?)"\s+title="([\d\D]*?)"\s+class="note">')
    detail =  detail_re.findall(values)
    if detail:

        gu_dict['detail_url'] = 'http://guba.eastmoney.com'+ detail[0][0]
        gu_dict['title'] = detail[0][1]
    else:
        detail_re = re.compile(r']\s+<a href="([\d\D]*?)"\s+title="([\d\D]*?)"\s+class="note">')
        detail = detail_re.findall(values)
        if detail:
            gu_dict['detail_url'] = 'http://guba.eastmoney.com' + detail[0][0]
            gu_dict['title'] = detail[0][1]
        else:
            gu_dict['detail_url'] = ''
            gu_dict['title'] = ''
    #  发布时间
    realtime_re = re.compile(r'<cite class="last">([\d\D]*?)</cite>')
    realtime = realtime_re.findall(values)
    gu_dict['realtime'] = realtime[0]
    # 作者
    author_re = re.compile(r'target="_blank"><font>([\d\D]*?)</font>')
    author = author_re.findall(values)
    gu_dict['author'] = author[0]
    gu_list.append(gu_dict)

for url in gu_list:
    detail_url = url.get('detail_url')
    content = requests.get(url=detail_url, headers=headers, proxies=proxy).content.decode('utf-8')
    comment_re = re.compile(r'id="zwcontent">[\d\D]*?</div>')

