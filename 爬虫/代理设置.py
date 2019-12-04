import random

import requests

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
            AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134"}
url = "https://www.kuaidaili.com/free/inha/3/"
proxies = [{"http":"115.221.243.207:9999",},
           {"http":"123.163.122.139:9999",},
           {"http":"58.22.177.191:9999",},
           {"http": "27.152.2.40:9999",},
           ]
proxy = random.choice(proxies)
print(proxy)
response = requests.request(url=url, method="get", headers=headers, proxies=proxy).content.decode("utf-8")
print(response)