import json

import requests

url = "https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start=0&limit={}"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
             AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134",}
content = requests.get(url=url.format(20), headers=headers).content.decode('utf-8')
data = json.loads(content)
# for movie in data:
#     title = movie.get('title')
#     score = movie.get('score')
#     release_date = movie.get('release_date')
#     movie_url = movie.get('url')
#     with open('movie.txt', 'a', encoding='utf-8' ) as fp:
#         fp.write("影片名:{}  评分:{} 上映时间:{}\n影片详细:{}\n".format(title, score, release_date, movie_url))
movie_list = []
movie_dict = {}
for movie in data:
    movie_dict['title'] = movie.get('title')
    movie_dict['score']  = movie.get('score')
    movie_dict['release_date']  = movie.get('release_date')
    movie_dict['movie_url']  = movie.get('url')
    movie_list.append(movie_dict)
# movie_json = json.dumps(movie_list, ensure_ascii=False)
# with open('movie.json', 'w', encoding='utf-8') as fp:
#     fp.write(movie_json)
with open('movie.json', 'w', encoding='utf-8') as fp:
    json.dump(movie_list,fp , ensure_ascii=False)
