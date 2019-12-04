import json
import random
import time
from lxml import etree
from selenium import webdriver

driver = webdriver.PhantomJS(executable_path=r'D:\环境文件\phantomjs-2.1.1-windows\bin\phantomjs.exe')
url = 'https://www.guazi.com/www/buy'
driver.get(url)
time.sleep(2)
num = 1
data = []
while True:
    tree = etree.HTML(driver.page_source)

    title_list = tree.xpath('//h2[@class="t"]/text()')

    data_list = tree.xpath('//div[@class="t-i"]/text()')

    price_list = tree.xpath('//div[@class="t-price"]/p/text()')

    detail_url_list = tree.xpath('//ul[@class="carlist clearfix js-top"]/li/a/@href')



    for i in range(len(title_list)):
        data_dict = {}
        data_dict['title'] = title_list[i]
        data_dict['data'] = data_list[i]+'|'+data_list[i+1]+'|'+data_list[i+2]
        data_dict['price']= price_list[i] + '万'

        detail_url = 'https://www.guazi.com'+detail_url_list[i]
        driver.get(detail_url)
        print(num)
        num += 1
        time.sleep(2)
        tree = etree.HTML(driver.page_source)
        hc = tree.xpath('//div[@class="right-carnumber"]/text()')[0]
        data_dict['hc'] = hc
        detail_data = tree.xpath('//ul[@class="assort clearfix"]/li/span/text()')
        print(detail_data)
        data_dict['create_time'] = detail_data[0]
        data_dict['mileage'] = detail_data[1]
        data_dict['Displacement'] = detail_data[2]
        data_dict['Gearbox'] = detail_data[3]
        service_guarantee = tree.xpath('//ul[@class="service-protect-list clearfix"]/li/span/text()')
        data_dict['service_guarantee'] = service_guarantee
        data.append(data_dict)
    print(data)
    try:
        url = tree.xpath('//a[@class="next"]/@href')[0]
        driver.get('https://www.guazi.com/'+ url)
        time.sleep(2)
    except:
        with open('two_car.json', 'w',encoding='utf-8' ) as fp:
            json.dump(data, fp,ensure_ascii=False)
        print('结束')
        break



