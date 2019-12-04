import requests

url ="https://security.kaixin001.com/login/login_post.php"
data = {"email":"18811176939",'password':"123457"}
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
              AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36"}
response = requests.request(method="post", headers=headers, url=url, data=data ).content.decode("utf-8")
with open("kaixin.html", "w", encoding="utf-8") as fp:
    fp.write(response)

