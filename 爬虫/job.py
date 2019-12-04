import json
import random
import re
import time
from selenium import webdriver

import requests
from lxml import etree
import pymysql

user = "root"
password = "123"
database = "apply"
host = "localhost"
db = pymysql.connect(user=user, password=password, database=database, host=host)
cursor = db.cursor()


url_start = "https://www.lagou.com/jobs/list_%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90%E5%B8%88?labelWords=&fromSearch=true&suginput="
url_parse = "https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false"
agent = [
    'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
    'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0',
    'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)',
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
    'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
    'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11',
    'Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; TencentTraveler 4.0)',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; The World)',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
]
headers = {
    "User-Agent": random.choice(agent),
    'Referer': 'https://www.lagou.com/jobs/list_%E8%BF%90%E7%BB%B4?city=%E6%88%90%E9%83%BD&cl=false&fromSearch=true&labelWords=&suginput=',
}

proxies = [
    {'http': 'http://111.29.3.185:8080'},
    {'http': 'http://111.29.3.190:8080'},
    {'http': 'http://111.29.3.220:8080'},

    {'http': 'http://111.29.3.195:80'},

    {'http': 'http://222.66.94.130:80'},
    {'http': 'http://117.88.177.192:3000'},
    {'http': 'http://39.137.69.8:8080'},

]
proxy = random.choice(proxies)
print(proxy)
for x in range(1, 31):
    data = {
        "first": "false",
        "pn": str(x),
        "kd": "python实习",
    }
    s = requests.Session()
    s.get(url_start, headers=headers,proxies=proxy, timeout=5)  # 请求首页获取cookies
    cookie = s.cookies  # 为此次获取的cookies
    response = s.post(url_parse, data=data, headers=headers, cookies=cookie,proxies=proxy, timeout=10).content.decode()  # 获取此次文本
    time.sleep(2)
    text = json.loads(response)
    print(response)
    show_id = text["content"]['showId']
    info = text["content"]["positionResult"]["result"]
    for i in info:
        proxy = random.choice(proxies)
        # 公司名称
        companyFullName = i["companyFullName"]

        # 职位名称
        positionName = i["positionName"]

        # 薪资水平
        salary = i["salary"]

        # 公司规模
        companySize = i["companySize"]


        # 发布时间
        createTime = i["createTime"]

        # 工作地点
        city = i["city"]
        district = i["district"]
        address = str(city)+str(district)

        # 职位要求
        workYear = i["workYear"]
        education = i["education"]

        # 公司类型
        financeStage = i["financeStage"]
        industryField = i["industryField"]
        genre = industryField + financeStage


        # url id
        positionId = i["positionId"]
        detail_url = "https://www.lagou.com/jobs/{}.html?show={}".format(positionId, show_id)
        s = requests.Session()

        s.get(detail_url, headers=headers, proxies=proxy, timeout=10)  # 请求首页获取cookies


        cookie = s.cookies  # 为此次获取的cookies
        print(proxy)
        content = requests.get(url=detail_url, headers=headers,cookies=cookie,proxies=proxy, timeout=10).content.decode('utf-8')
        tree = etree.HTML(content)
        time.sleep(2)
        # 职位描述
        # print(detail_url)
        # job_detail_box = re.findall(r'<div class="job-detail">([\d\D]*?)</div>', content)
        # time.sleep(3)
        # try:
        #     info = re.findall(r'[\u4e00-\u9fa5]+', job_detail_box[0])
        #     print(info)
        # except:
        #     with open('errorpage.html', 'w', encoding='utf-8') as fp:
        #         fp.write(content)
        #     exit()
        info = tree.xpath('//div[@class="job-detail"]//p/text()')
        if info:
            message = info
        else:
            message = '未知'


        crawl_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        crawl_name = "再渐"
        sql = 'insert into python实习(companyFullName, positionName, salary, companySize, createTime, address, genre, info, crawl_name, crawl_time) values("{}","{}","{}","{}","{}","{}","{}","{}","{}","{}")'.format(companyFullName, positionName, salary, companySize, createTime, address, genre, pymysql.escape_string(str(message)), crawl_name, crawl_time)
        cursor.execute(sql)
        db.commit()
cursor.close()
db.close()









