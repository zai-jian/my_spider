import json

import requests
def translates(query):
    url = "https://fanyi.baidu.com/v2transapi?from=en&to=zh"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
                AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36"}
    data = {"query": query,"token": "3e02961a4bac4a01750666714092c0f5","sign": "625272.878921","simple_means_flag": "3","transtype": "realtime"}
    response = requests.request(method="post", url=url, data=data, headers=headers).content.decode("utf-8")
    response = json.loads(response)
    print(response)

def main():
    kw = str(input("请输入要翻译的句子"))
    translates(kw)

if __name__ == '__main__':
    while True:
        main()