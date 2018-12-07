from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains#控制鼠标移动的模块
import selenium.webdriver.support.ui as ui
import requests
import unittest

from 摩尔精英测试框架.config.登陆 import 登陆


class 更改设置(unittest.TestCase):
    def setUp(self):   #点击摩尔精英集团
        self.sss=登陆().首页测试()
        sleep(1)
    def test_1(self):
        self.sss.find_element_by_xpath('/html/body/div[3]/div[2]/div[1]/div[1]/a[1]').click()
        sleep(2)
        wd1 = self.sss.window_handles
        self.sss.switch_to.window(wd1[-1])
        a = self.sss.title
        self.assertEqual(a,'摩尔精英官网-让中国没有难做的芯片')
        print('有摩尔精英官网')
        sleep(2)
        wd1 = self.sss.window_handles
        self.sss.switch_to.window(wd1[-1])
        # self.sss.quit()#关闭当前的窗口


    def test_2(self):   #测试是否能搜索到软件测试软件
        self.sss.find_element_by_xpath('//*[@id="searchform"]/input[1]').send_keys('软件测试')
        sleep(2)
        self.sss.find_element_by_xpath('//*[@id="search-submit"]').click()
        sleep(2)
        a=self.sss.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/span[2]').text
        self.assertEqual(a,'软件测试')
        print('有这个软件测试')
        sleep(2)
        self.sss.back()

    def test_3(self):    #测试能否出现二维码扫描窗口
        self.sss.find_element_by_xpath('//*[@id="qr"]/a').click()
        sleep(2)
        a=self.sss.find_element_by_xpath('/html/body/div[1]/div[1]/div[1]/p').text
        self.assertEqual(a,'扫描关注摩尔精英招聘')
        sleep(2)
        print('能出现二维码')

    def test_4(self):     #测试能否回到顶部
        js = "var q=document.documentElement.scrollTop=10000"  # 控制滚动条的JavaScript代码       10000表示的是：页面的高度，数字越大，滚动条越往下
        self.sss.execute_script(js)
        sleep(2)
        self.sss.find_element_by_xpath('//*[@id="gotoTop"]/a').click()
        print(js)
        js = "var q=document.documentElement.scrollTop=0"
        # self.assertTrue(s)
        print('成功')

    def test_5(self):
        self.sss.find_element_by_xpath('//*[@id="talk"]/a').click()
        sleep(2)
        a=self.sss.find_element_by_xpath('//*[@id="feed-form"]/div[3]/span').text
        self.assertEqual(a,'确定')
        print('可以输入意见和邮箱')





    def tearDown(self):
        sleep(1)
        self.sss.quit()

if __name__=='__main__':
    unittest.main()























