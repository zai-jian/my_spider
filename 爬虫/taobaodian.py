import json
import re

from spider_res import request
from lxml import etree

url_list = [
    'https://tce.taobao.com/api/mget.htm?callback=jsonp1671&tce_sid=1870342,1871657&tce_vid=2,2&tid=,&tab=,&topic=,&count=,&env=online,online',
    'https://tce.taobao.com/api/mget.htm?callback=jsonp1588&tce_sid=1870343,1871658&tce_vid=2,2&tid=,&tab=,&topic=,&count=,&env=online,online',
    'https://tce.taobao.com/api/mget.htm?callback=jsonp1758&tce_sid=1870341,1871659&tce_vid=2,2&tid=,&tab=,&topic=,&count=,&env=online,online',
    'https://tce.taobao.com/api/mget.htm?callback=jsonp1845&tce_sid=1870340,1871656&tce_vid=2,2&tid=,&tab=,&topic=,&count=,&env=online,online',
    'https://tce.taobao.com/api/mget.htm?callback=jsonp1932&tce_sid=1870333,1871655&tce_vid=2,2&tid=,&tab=,&topic=,&count=,&env=online,online',
    'https://tce.taobao.com/api/mget.htm?callback=jsonp2019&tce_sid=1870321,1871654&tce_vid=2,2&tid=,&tab=,&topic=,&count=,&env=online,online',
    'https://tce.taobao.com/api/mget.htm?callback=jsonp2106&tce_sid=1870316,1871653&tce_vid=2,2&tid=,&tab=,&topic=,&count=,&env=online,online',
]

for url in url_list:
    content = request(url)
    json_re = re.findall(r'({.*})',content)[0]
    tce_id = re.findall(r'tce_sid=(\d*)',url)[0]
    print(json_re)
    info_dict = json.loads(json_re)
    print(info_dict)
    result = info_dict["result"][tce_id]['result']
    for info in result:
        item_current_price = info['item_current_price']
        item_pic ='https:'+ info['item_pic']
        item_title = info['item_title']
        item_url = 'http:'+info['item_url']
        print('标题:'+item_title)
        print('价格: '+item_current_price)
        print('图片: '+item_pic)
        print('详细页面: '+item_url)
        # with open('tianmao.txt', 'a',encoding="utf-8") as fp:
        #     fp.write('标题:'+item_title+'\n'+'价格: '+item_current_price+'\n'+'图片: '+item_pic+'\n'+'详细页面: '+item_url+'\n')






