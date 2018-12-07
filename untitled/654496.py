from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains#控制鼠标移动的模块
import re
dr=webdriver.Chrome()
dr.get('https://www.baidu.com')
sleep(2)
dr.find_element_by_xpath('//*[@id="kw"]').send_keys('美女野兽')
sleep(2)
dr.find_element_by_xpath('//*[@id="su"]').click()
sleep(2)
dr.find_element_by_xpath('//*[@id="1"]/h3/a').click()
sleep(5)
dr.find_element_by_xpath('')