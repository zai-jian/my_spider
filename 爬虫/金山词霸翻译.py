import json
import random

import requests
def translate(w):
    translates = ''
    url = "http://fy.iciba.com/ajax.php?a=fy"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
                  AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36"}
    proxies = [{"http":"115.221.243.207:9999",},
               {"http":"123.163.122.139:9999",},
               {"http":"58.22.177.191:9999",},
               {"http": "27.152.2.40:9999",},
               ]

    data = {
        'w':w,
    }
    proxy = random.choice(proxies)
    response  = requests.request(url=url, headers=headers, method="post",data=data).content.decode("utf-8")
    response = json.loads(response)
    for i in response["content"]["word_mean"]:
        translates += "{}\n".format(i)
    print("{}\n{}".format(w, translates))
    with open("word.txt".format(w), 'a', encoding="utf-8") as fp:
        fp.write("{}\n{}".format(w, translates))

def main():
    w = input("请输入单词")
    translate(w)

if __name__ == '__main__':
    while True:
        main()