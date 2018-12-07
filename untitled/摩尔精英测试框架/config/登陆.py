from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains#控制鼠标移动的模块
import selenium.webdriver.support.ui as ui
class 登陆():
    def 账号(self):
        dr=webdriver.Chrome()
        dr.get('http://www.moore.ren/')
        sleep(2)
        dr.find_element_by_xpath('//*[@id="user-nomal"]/div[3]/div[1]/li[1]/a').click()
        wd = dr.window_handles
        dr.switch_to_window(wd[1])
        dr.find_element_by_xpath('//*[@id="emailInput"]').send_keys(15837806865)
        sleep(2)
        dr.find_element_by_xpath('//*[@id="passwordInput"]').send_keys(15837806865)
        sleep(2)
        dr.find_element_by_xpath('//*[@id="userForm"]/input[1]').click()
        sleep(2)
        dr.find_element_by_xpath('//*[@id="login-name"]/a').click()
        sleep(2)
        dr.find_element_by_xpath('//*[@id="top_right"]/li[1]/a').click()
        sleep(2)
        return dr

    def 首页测试(self):
        dr=webdriver.Chrome()
        dr.get('http://www.moore.ren/')
        sleep(2)
        return dr


# aa=登陆()
# aa.账号登陆('http://www.moore.ren/')






