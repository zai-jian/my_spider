import re

from selenium import webdriver
from lxml import etree
driver = webdriver.PhantomJS(executable_path=r'D:\环境文件\phantomjs-2.1.1-windows\bin\phantomjs.exe')
url = 'https://search.douban.com/book/subject_search?search_text=python&cat=1001'
driver.get(url)
with open('book.html', 'w',  encoding='utf-8') as fp:
    fp.write(driver.page_source)

tree = etree.HTML(driver.page_source)
book = tree.xpath('//div[@class="item-root"]//div[@class="title"]/a/text()')
print(book)