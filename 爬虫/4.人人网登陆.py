import requests

url = "http://www.renren.com/PLogin.do"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
              AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36"}

data = {'email':'17803373056', "password":"13483648816"}
response = requests.request(method="post", url=url, data=data, headers=headers).content.decode("utf-8")

with open("renren.html", "w", encoding="utf-8") as fp:
    fp.write(response)