from spider_res import request
from lxml import etree
url = 'https://bj.fang.lianjia.com/loupan/'
def xml(url):
    content = request(url)
    tree = etree.HTML(content)
    return tree
tree = xml(url)
# 所有城市url 列表
city_list = tree.xpath('//div[@class="fc-main clear"]//a/@href')
for url in city_list:
    de_url = "https:"+url+"/loupan/"
    print(de_url)
    tree = xml(de_url)
    # 城市有多少页楼盘
    hotel_nums = tree.xpath('//div[@class="resblock-have-find"]/span[@class="value"]/text()')[0]
    nums = int(hotel_nums)//10 + 1
    for num in range(1,nums+1):
        pg_url = de_url + "pg{}".format(num)
        print(pg_url)
        tree = xml(pg_url)

        # 楼盘列表盒子
        hotel_box = tree.xpath('//ul[@class="resblock-list-wrapper"]/li')

        for info in hotel_box:
            # 楼盘图片
            img = info.xpath('.//img/@data-original')[0]

            # 楼盘名称
            title = info.xpath('./a/@title')[0]

            # 楼盘所在区域
            address1 = info.xpath('./div/div[@class="resblock-location"]/span/text()')
            address2 = info.xpath('./div/div[@class="resblock-location"]/a/text()')
            detail_address = address1[0] +'/'+ address1[1] +'/'+address2[0]

            # 楼盘建面
            try:
                are = info.xpath('.//div[@class="resblock-area"]/span/text()')[0]
            except:
                are = "none"

            # 楼盘详细url
            url = info.xpath('./a/@href')[0]
            detail_url = 'https://bj.fang.lianjia.com/' + url
            detail_content = request(detail_url)
            detail_tree = etree.HTML(detail_content)

            # 楼盘详细图片
            detail_img = detail_tree.xpath('//ul[@class="col-nav carousel-body animation"]//img/@src')

            # 户型盒子
            try:
                form_list = detail_tree.xpath('.//div[@class="houselist frame-container carousel"]//li[@data-index="0"]')[1]
            except:
                form_list = detail_tree.xpath('.//div[@class="houselist frame-container carousel"]//li[@data-index="0"]')[0]
            #户型
            form = form_list.xpath('.//div[@class="content-title"]/text()')
            form_ls = []
            for i in form:
                form_ls.append(i.strip())
            # 朝向面积
            direction = form_list.xpath('.//div[@class="content-area"]/text()')
            direction_lst = []
            for i in direction:
                if i.find('向') != -1:
                    direction_lst.append(i.strip())


            # 楼盘info 盒子
            info_box = detail_tree.xpath('//div[@class="resblock-info animation qr-fixed "]')[0]

            # 楼盘均价价格
            price_list1 = info_box.xpath('.//span[@class="price-number"]/text()')
            price_list2 = info_box.xpath('.//span[@class="price-unit"]/text()')
            price_list = []
            for i in range(len(price_list1)):
                try:
                    price_list.append(price_list1[i]+price_list2[i])
                except:
                    price_list.append("none")



            # 项目地址
            pro_address = info_box.xpath('.//li[@class="info-item"]//span[@class="content"]/text()')[0]

            # 最新开盘
            new_open = info_box.xpath('.//li[@class="info-item open-date-wrap"]//span[@class="content"]/text()')[0]

            # 详细信息链接
            detail_info_url = info_box.xpath('.//div[@class="more-building"]//a/@href')[0]
            detail_info_url = "https://bj.fang.lianjia.com/"+ detail_info_url
            detail_info_content = request(detail_info_url)
            detail_info_tree = etree.HTML(detail_info_content)

            # 信息大盒子
            big_info_box = detail_info_tree.xpath('//div[@class="big-left fl"]')[0]

            # 详细信息
            detail_info1 = big_info_box.xpath('.//ul[@class="x-box"]//span/text()')
            # detail_info2 = big_info_box.xpath('.//ul[@class="x-box"]//span[@class="label-val"]/text()')
            detail_info_list = []
            for i in detail_info1:
                a = i.strip()
                if a and a!="楼盘户型：" and a!= '周边规划：':
                    detail_info_list.append(a)

            with open('lianjia.txt', 'a', encoding='utf-8') as fp:
                fp.write("楼盘名称: "+str(title)+'\n'+'楼盘图片: '+str(img)+'\n'+'楼盘建面: '+str(are)+'\n'+'楼盘所在区域: '+str(detail_address)+'\n'+'楼盘价格: '+str(price_list)+'\n'+"户型: "+str(form_ls)+'\n'+'面积朝向: '+str(direction_lst)+'\n'+'楼盘所在区域: '+str(pro_address)+'\n'+'最新开盘时间: '+str(new_open)+'\n'+'详细信息: '+str(detail_info_list)+'\n')



