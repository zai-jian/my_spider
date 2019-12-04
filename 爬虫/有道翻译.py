import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from lxml import etree
def translate(word):
    driver = webdriver.PhantomJS(executable_path=r'D:\环境文件\phantomjs-2.1.1-windows\bin\phantomjs.exe')
    url = 'http://fanyi.youdao.com/'
    driver.get(url)
    driver.find_element_by_id('inputOriginal').send_keys(Keys.CONTROL,'a')
    driver.find_element_by_id('inputOriginal').send_keys(Keys.BACK_SPACE)
    driver.find_element_by_id('inputOriginal').send_keys('{}'.format(word))
    time.sleep(2)
    driver.save_screenshot('1.png')
    tree = etree.HTML(driver.page_source)
    translate = tree.xpath('//div[@class="input__target__dict"]//span[@class="no-link"]/text()')
    print(translate)

if __name__ == '__main__':
    while  True:
        word = input("请输入单词")
        translate(word)


