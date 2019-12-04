import time

from lxml import etree
from selenium import webdriver

def main():
    driver = webdriver.PhantomJS(executable_path=r'D:\环境文件\phantomjs-2.1.1-windows\bin\phantomjs.exe')
    url = 'https://www.douyu.com/directory/all'
    driver.get(url)
    time.sleep(3)
    num = 1
    print(num)
    while True:
        tree = etree.HTML(driver.page_source)
        anchor_list = tree.xpath('//div[@class="layout-Module-container layout-Cover ListContent"]//div[@class="DyListCover-info"]//text()')
        url_list = tree.xpath('//div[@class="layout-Module-container layout-Cover ListContent"]/ul/li/div/a[1]/@href')
        detail_list = []
        for i in range(0, len(anchor_list),4):
            detail_list.append(anchor_list[i:i+4])
        for i in range(len(url_list)):
            detail_list[i].append('https://www.douyu.com/'+url_list[i])
        print(detail_list)
        aria_disabled = tree.xpath('//li[@title="下一页"]/@aria-disabled')[0]
        if aria_disabled == "false":
            driver.find_element_by_class_name("dy-Pagination-next").click()
            time.sleep(3)
            num +=1
            print(num)
        else:
            print('结束 页数{}'.format(num))
            return

if __name__ == '__main__':
    main()