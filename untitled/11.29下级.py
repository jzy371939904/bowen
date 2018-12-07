from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains#控制鼠标移动的模块
import selenium.webdriver.support.ui as ui
import requests
import unittest


dr=webdriver.Chrome()#打开浏览器
dr.get('http://i.qq.com')
sleep(2)
dr.switch_to_frame('login_frame')
dr.find_element_by_xpath('//*[@id="switcher_plogin"]').click()
sleep(2)
dr.find_element_by_xpath('//*[@id="u"]').send_keys(2132321321)
sleep(2)
dr.find_element_by_xpath('//*[@id="p"]').send_keys(444421)
sleep(2)
dr.find_element_by_xpath('//*[@id="login_button"]').click()
sleep(10)

wd1=dr.find_element_by_xpath('//*[@id="newVcodeIframe"]/iframe')
dr.switch_to_frame(wd1)
start=dr.find_element_by_xpath('//*[@id="tcaptcha_drag_thumb"]')
ActionChains(dr).drag_and_drop_by_offset(start,188,0).perform()
sleep(10)

