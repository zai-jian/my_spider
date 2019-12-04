import random
import re

import requests

url = "http://www.iltaw.com/animal/all?page=2"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
            (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
}
proxies = [{'http':'111.29.3.185:8080'},
            {'https':'27.152.91.157:9999'},
            {'http':'111.29.3.220:8080'},
            {'https':'113.124.92.35:9999'},
            {'http':'111.29.3.195:80'},
            {'https':'120.79.214.236:8000'},

           ]
proxy = random.choice(proxies)
print(proxy)
content = requests.get(url=url, headers=headers, proxies=proxy).content.decode('utf-8')
img_re = re.compile(r'data-url="(http://image.iltaw.com/[\d\D]*?.jpg)"')
img_list = img_re.findall(content)
print(img_list)
# for i,img_url in enumerate(img_list):
#     content = requests.get(url=img_url, headers=headers, proxies=proxy).content
#     with open(r'img/ani{}.png'.format(i), 'wb') as fp:
#         fp.write(content)

