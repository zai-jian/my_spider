def request(url):
    import requests
    import random
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
            (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
               'Cookie': 'JSESSIONID=ABAAABAAAGFABEF400B0F651B3EE5B8D7DDD0A3768B9948; WEBTJ-ID=20191128185841-16eb1a9bdc7387-0a45caba67b422-2393f61-1327104-16eb1a9bdc8680; _ga=GA1.2.607056457.1574938722; _gid=GA1.2.652751490.1574938722; user_trace_token=20191128185841-09f5101d-11ce-11ea-a9ef-525400f775ce; LGUID=20191128185841-09f512b1-11ce-11ea-a9ef-525400f775ce; index_location_city=%E5%85%A8%E5%9B%BD; _gat=1; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1574938722,1574946478; LGSID=20191128210757-18aa4561-11e0-11ea-a68a-5254005c3644; PRE_UTM=; PRE_HOST=link.zhihu.com; PRE_SITE=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fwww.lagou.com%2F; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F; TG-TRACK-CODE=index_search; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2216eb220329f48-0e70278c466bf3-2393f61-1327104-16eb22032a0461%22%2C%22%24device_id%22%3A%2216eb220329f48-0e70278c466bf3-2393f61-1327104-16eb22032a0461%22%7D; sajssdk_2015_cross_new_user=1; SEARCH_ID=969025a863054d09b11f30487ba02c9d; gate_login_token=f94e93ac44c9ff3fa8f53d87dcfbd2ba1a42a30238b54dce2ef9ef849765c3d6; _putrc=01412E925BC0041E123F89F2B170EADC; login=true; unick=%E7%94%A8%E6%88%B73056; privacyPolicyPopup=false; hasDeliver=0; X_HTTP_TOKEN=c9eb90e5b859dc5e2086494751ae6db610d02caf5f; LGRID=20191128211322-daa4d12e-11e0-11ea-a68a-5254005c3644; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1574946804'
    }
    proxies = [{'http':'http://111.29.3.185:8080'},
                {'http':'http://106.42.217.216:9999'},
                {'http':'http://111.29.3.220:8080'},
                {'http':'http://58.211.134.98:38480'},
                {'http':'http://111.29.3.195:80'},
                {'http':'http://58.253.158.189:9999'},
                {'http':'http://222.66.94.130:80'},
                {'http':'http://114.55.95.112:8999'},
                {'http':'http://39.137.69.8:8080'},
                {'https':'http://122.70.148.66:808'},
       ]
    proxy = random.choice(proxies)
    print(proxy)
    content = requests.get(url=url, headers=headers, proxies=proxy).content.decode('utf8')
    return content

