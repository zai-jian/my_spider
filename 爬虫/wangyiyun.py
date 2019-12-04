import random
from lxml import etree
import requests


class wangyi:
    def __init__(self, url='https://music.163.com/discover/artist'):
        self.tree = self.request_html(url)
        self.parse_html()
        pass

    def request_html(self, url):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
              AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36"}
        proxies = [
            {'http': 'http://111.29.3.185:8080'},
            {'http': 'http://106.42.217.216:9999'},
            {'http': 'http://111.29.3.220:8080'},
            {'http': 'http://58.211.134.98:38480'},
            {'http': 'http://111.29.3.195:80'},
            {'http': 'http://58.253.158.189:9999'},
            {'http': 'http://222.66.94.130:80'},
            {'http': 'http://114.55.95.112:8999'},
            {'http': 'http://39.137.69.8:8080'},
            {'https': 'http://117.57.91.136:9999'},
                   ]
        proxy = random.choice(proxies)
        print(proxy)
        content = requests.request(url=url, headers=headers, proxies=proxy, method='get').content.decode('utf-8')
        tree = etree.HTML(content)

        return tree

    def parse_html(self):
        id = self.tree.xpath('//div[@class="blk"]//a/@data-cat')
        name = self.tree.xpath('//div[@class="blk"]//a/text()')
        for id , name in zip(id,name):
            print("-------------------" +name+"-------------------")
            artist_url = "https://music.163.com/discover/artist/cat?id={}".format(id)
            tree = self.request_html(artist_url)
            url = tree.xpath('//ul[@class="n-ltlst f-cb"]//li/a[@class]/@href')[1:]
            for i in url:
                full_url = "https://music.163.com"+i
                tree = self.request_html(full_url)
                title = tree.xpath('//a[@class="nm nm-icn f-thide s-fc0"]/@title')
                singer_url = tree.xpath('//a[@class="nm nm-icn f-thide s-fc0"]/@href')
                for i,j in zip(title,singer_url):
                    singer_url = "https://music.163.com"+j
                    print(i +": "+  singer_url)



        pass

if __name__ == '__main__':
    wangyi()