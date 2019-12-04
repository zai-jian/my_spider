import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(executable_path=r'D:\环境文件\phantomjs-2.1.1-windows\bin\phantomjs.exe')

url = 'https://www.baidu.com'
driver.get(url=url)



driver.find_element_by_id('kw').send_keys('弟弟')
driver.find_element_by_id('su').click()
driver.find_element_by_id('kw').send_keys(Keys.CONTROL,'a')
time.sleep(1)
driver.find_element_by_id('kw').send_keys(Keys.BACK_SPACE)
driver.find_element_by_id('kw').send_keys('哥哥')
time.sleep(1)
driver.find_element_by_id('su').click()
time.sleep(2)
