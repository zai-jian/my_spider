import requests

#  url :
#  https://tieba.baidu.com/f?kw=%E5%8D%A1&ie=utf-8&pn=50
#  'java' : 'http://tieba.baidu.com/f?ie=utf-8&kw=java&fr=search'
#  'python': 'http://tieba.baidu.com/f?ie=utf-8&kw=python&fr=search'
#  'c++':'http://tieba.baidu.com/f?ie=utf-8&kw=c%2B%2B&fr=search'



# 爬取百度贴吧前十页
def spider_tieba(kw):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
         AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36"}

    url = "https://tieba.baidu.com/f?kw={}&ie=utf-8&pn=".format(kw)

    for page in range(10):
        full_url = url + str(page * 50)
        response = requests.get(url=full_url, headers=headers).content.decode('utf-8')
        with open('{}吧{}.html'.format(kw, page + 1), 'w', encoding='utf-8') as fp:
            fp.write(response)
#  补充
#  params =  { 'ie': 'utf-8'
# 'kw': 'c++'
# 'fr': 'search' }
# 加了params就可以把url?后边的内容全部删除只要再传参的时候传入params就可以了
#  requests.request(method="get", url=full_url,params=params,headers=headers)
def main():
    kw = input("请输入贴吧名字")
    spider_tieba(kw)

if __name__ == '__main__':
    main()