import json
import re

import requests

url = "https://zu.fang.com/"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
            (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
}
content = requests.get(url=url, headers=headers).content.decode('gbk')
dd_re = re.compile(r'<dl class="list hiddenMap rel">[\d\D]*?</dl>')
data = dd_re.findall(content)
home_list = []
for home in data:
    home_dict = {}
    # print(home)
    title_re = re.compile('target="_blank" title="(.*?)">')
    title = title_re.findall(home)[0]
    home_dict['title'] = title
    img_re = re.compile('usertype="1" data-src="(.*?)"')
    img = img_re.findall(home)[0]
    home_dict['img'] = img
    info_re = re.compile(r'(\S*?)<span class="splitline">\|</span>(.*?)<span class="splitline">\|</span>(.*?)<span class="splitline">\|</span>([\S\s]*?)\r')
    info = info_re.findall(home)
    home_dict['info'] = info[0][0]+'|'+info[0][1]+'|'+info[0][2]+'|'+info[0][3]
    place_re = re.compile(r'target="_blank"><span>(.*?)</span></a>-<a href="[\d\D]*?" target="_blank"><span>(.*?)</span></a>-<a href="[\d\D]*? target="_blank"><span>(.*?)</span></a><')
    place = place_re.findall(home)
    home_dict['place'] = place[0][0]+'-'+place[0][1]+'-'+place[0][2]
    price_re = re.compile(r'<p class="mt5 alingC"><span class="price">(.*?)</span>')
    price = price_re.findall(home)[0]
    home_dict['price'] = price+'元每月'
    home_list.append(home_dict)
with open('home_info.json', 'w', encoding='utf-8') as fp:
    json.dump(home_list, fp, ensure_ascii=False)







