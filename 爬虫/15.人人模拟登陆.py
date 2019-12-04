import time

from lxml import etree
from selenium import webdriver

driver = webdriver.PhantomJS(executable_path=r'D:\环境文件\phantomjs-2.1.1-windows\bin\phantomjs.exe')
url = 'http://www.renren.com/'
driver.get(url)

driver.find_element_by_name('email').clear()

driver.find_element_by_name('email').send_keys('17803373056')
time.sleep(2)
driver.find_element_by_name('password').send_keys('123')
driver.find_element_by_id('login').click()
time.sleep(2)
driver.save_screenshot('p2.png')