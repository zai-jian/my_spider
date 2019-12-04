import json

import requests
def translates(kw):
    url = "https://fanyi.baidu.com/sug"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
                AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36"}
    data = {"kw": kw}
    response = requests.request(method="post", url=url, data=data, headers=headers).content.decode("utf-8")
    response = json.loads(response)
    for i in response["data"]:
        word= i["k"]
        translate = i["v"]
        print("{} : {}".format(word, translate))

def main():
    kw = input("请输入要翻译的单词")
    translates(kw)

if __name__ == '__main__':
    while True:
        main()