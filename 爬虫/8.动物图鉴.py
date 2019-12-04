import random
import re

import requests

url = "http://www.iltaw.com/animal/{}"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
            (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
}
# proxies = [{'http':'221.1.200.242:50069'},
#             {'http':'114.239.151.101:9999'},
#             {'http':'36.25.43.122:9999'},
#             {'http':'163.125.113.224:8118'},
#             {'http':'171.13.202.99:9999'},
#            ]
# proxy = random.choice(proxies)
for num in range(10):
    content = requests.get(url=url.format(num+1), headers=headers).content.decode('utf-8')

    summary_re = re.compile(r'<p>(.*?)；<br />(.*?)；<br />学名：<em>(.*?)</em>。<br />(.*?)<br />|<strong>中文名：</strong>(.*?)；<br /><strong>英文名：</strong>(.*?)；<br /><strong>学名：</strong><em>(.*?)</em>。<br />(.*?)<br />|<strong>中文名：</strong>(.*?)；<br /><strong>英文名：</strong>(.*?)；<br /><strong>学名：</strong><em>(.*?)</em>。<br />(.*?)</p>')
    summary_list = summary_re.findall(content)
    print(summary_list)
# with open('animals.html', 'w', encoding='utf-8') as fp:
#     fp.write(content)

