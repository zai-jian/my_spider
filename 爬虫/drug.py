import random
import re

import pymysql
import requests
user = 'root'
password = '123'
host = 'localhost'
port = 3306
database = "durg"
db = pymysql.connect(user=user, password=password, host=host, port=port, database=database)
cursor = db.cursor()
url = 'https://www.111.com.cn/categories/953710-j1.html'
def request(url):
    import requests
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
            (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
    }
    proxies = [{'http':'111.29.3.185:8080'},
                {'http':'106.42.217.216:9999'},
                {'http':'111.29.3.220:8080'},
                {'http':'58.211.134.98:38480'},
                {'http':'111.29.3.195:80'},
                {'http':'58.253.158.189:9999'},
       ]
    proxy = random.choice(proxies)
    print(proxy)
    content = requests.get(url=url, headers=headers, proxies=proxy).content.decode('gbk')
    return content


content = request(url)

detail_re = re.compile(r'<div isrecom="0" comproid=".*?" itemid=".*?" class="itemSearchResultCon">([\d\D]*?</spa)')
detail = detail_re.findall(content)
# print(detail)
# drug_url_re = re.compile(r'<a href="([\d\D]*?)" target="_blank"')
# drug_url = drug_url_re.findall(detail[0])
# price_re = re.compile(r'<span>\s+([\d\D]*?)\s+<')
# price = price_re.findall(detail)


for value in detail:
    v_list = []
    # 价格
    price_re = re.compile(r'<span>\s+([\d\D]*?)\s+<')
    price = price_re.findall(value)[0]
    # 详细地址
    drug_url_re = re.compile(r'<a href="([\d\D]*?)" target="_blank"')
    drug_url = drug_url_re.findall(value)
    drug_detail_url = "https:" + drug_url[0]
    content = request(drug_detail_url)
    # 药品标题
    title_re = re.compile(r'<h1>(.*?)</h1>')
    title = title_re.findall(content)[0]
    # 药品详细
    info_re = re.compile(r'<table>([\d\D]*?)</table>')
    info = info_re.findall(content)[0]
    # print(info)
    values_re = re.compile(r'<th>([\d\D]*?)</th>\s+<td[\d\D]*?>([\d\D]*?)</td>')
    values_list = values_re.findall(info)
    for i in values_list:
        v1 = i[0].strip().replace('(<a style="color:#0083ce" href="http://app1.sfda.gov.cn/datasearch/face3/dir.html" target="_blank">','').replace('</a>)','').replace(r"\u3000", '')
        v2 = i[1].strip().replace('(<a style="color:#0083ce" href="http://app1.sfda.gov.cn/datasearch/face3/dir.html" target="_blank">','').replace('</a>)','').replace(r"\u3000", '')
        v_list.append(v1+v2)
    sql = 'insert into durg(title, info, price) values("{}", "{}", "{}") '.format(title,v_list,price)
    cursor.execute(sql)
    db.commit()
cursor.close()
db.close()




