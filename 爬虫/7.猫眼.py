import json
import random

import requests
import re

url = "https://maoyan.com/board"

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
            (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
}
proxies = [{'http':'221.1.200.242:50069'},
            {'http':'114.239.151.101:9999'},
            {'http':'36.25.43.122:9999'},
            {'http':'163.125.113.224:8118'},
            {'http':'171.13.202.99:9999'},
           ]
proxy = random.choice(proxies)
print(proxy)
content = requests.get(url=url, headers=headers, proxies=proxy, timeout=5).content.decode('utf-8')
# with open('maoyan.html', 'w', encoding='utf-8') as fp:
#     fp.write(content)
movie_list = []

dd_re = re.compile(r'<dd>[\d\D]*?</dd>')
data = dd_re.findall(content)
for movie in data:
    movie_dict = {}
    title_re = re.compile(r' data-val="{movieId:\d*?}">(.*?)</a></p>')
    title = title_re.findall(movie)[0]
    movie_dict['title'] = title
    print(title)
    star_re = re.compile(r'<p class="star">([\d\D]*?)</p>')
    star = star_re.findall(movie)[0].split('\n')[1].replace(' ','')
    movie_dict['star'] = star
    print(star)
    score_re = re.compile(r'<p class="score"><i class="integer">(\d\.)</i><i class="fraction">(\d)</i></p>')
    score = score_re.findall(movie)[0][0]+score_re.findall(movie)[0][1]
    movie_dict['score'] = score
    print(score)
    rank_re = re.compile(r'<i class="board-index board-index-\d*?">(\d*?)</i>')
    rank = rank_re.findall(movie)[0]
    movie_dict['rank'] = rank
    print(rank)
    img_re = re.compile(r'<img data-src="(.*?)" alt=".*?" class="board-img" />')
    img = img_re.findall(movie)[0]
    movie_dict['img'] = img
    print(img)
    movie_list.append(movie_dict)

with open('maoyan.json', 'w', encoding='utf-8') as fp:
    json.dump(movie_list, fp, ensure_ascii=False)