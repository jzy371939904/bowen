from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains#控制鼠标移动的模块
import selenium.webdriver.support.ui as ui
import requests
import unittest

from 摩尔精英测试框架.config.登陆 import 登陆


class 更改设置(unittest.TestCase):
    sss=登陆().账号
    def test_1(self):
        self.sss.find_element_by_xpath('//*[@id="newpasswordform"]/div/div[2]/div/input').send_keys(15837806865)
        sleep(2)
        self.sss.find_element_by_xpath('//*[@id="firstpassword"]').send_keys(15837806865)
        sleep(2)
        self.sss.find_element_by_xpath('//*[@id="newpasswordform"]/div/div[7]/div/input').send_keys(15837806865)
        sleep(2)
        self.sss.find_element_by_xpath('//*[@id="newpasswordform"]/div/a').click()
        sleep(2)
        a=self.sss.title
        print(a)
        self.assertEqual('个人用户修改密码成功',a)
        sleep(2)
        print('修改密码成功')
        sleep(2)
        self.sss.back()


# if __name__=='__main__':

    def test_2(self):
        # self.sss.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/dl/dd[3]/a').click()
        # sleep(2)
        self.sss.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/dl/dd[2]/a').click()
        sleep(2)
        # self.sss.find_element_by_xpath('//*[@id="emailadd"]').click()
        # sleep(2)
        # self.sss.find_element_by_xpath('//*[@id="modify-mail-box"]/div[2]/input').send_keys('371939904@qq.com')
        # sleep(2)
        # self.sss.find_element_by_xpath('//*[@id="modify-mail-box"]/div[3]/a[1]').click()
        # sleep(2)
        a=self.sss.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div[2]/li[1]/a').text
        self.assertEqual(a,'更换邮箱')
        print('可以更换邮箱')
        sleep(2)
        self.sss.back()


    def test_3(self):
        self.sss.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/dl/dd[2]/a').click()
        sleep(2)
        a=self.sss.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div[2]/li[2]/a').text
        self.assertEqual(a,'更换手机号')
        print('可以更改手机')
        sleep(2)
        self.sss.back()


    def test_4(self):
        self.sss.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/dl/dd[2]/a').click()
        sleep(2)
        a=self.sss.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div[2]/li[4]/a').text
        self.assertEqual(a,'重新绑定')
        print('可以重新绑定微信')
        sleep(2)
        self.sss.back()


    def test_5(self):
        self.sss.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/dl/dd[2]/a').click()
        sleep(2)
        a=self.sss.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div[2]/li[3]/a').text
        self.assertEqual(a,'绑定Linkedin账号')
        print('绑定Linkedin账号成功')
        sleep(2)
        self.sss.back()


    def test_6(self):
        self.sss.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/dl/dd[3]/a').click()
        a=self.sss.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/a').text
        self.assertEqual(a,'保存')
        print('可以屏蔽公司后缀')
        sleep(2)
        self.sss.back()
# if __name__=='__main__':
#     unittest.main()




















