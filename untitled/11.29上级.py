from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains#控制鼠标移动的模块
import selenium.webdriver.support.ui as ui
import requests
import unittest

class  jd(unittest.TestCase):
    def test_1(self):

        dr=webdriver.Firefox()

        dr.get('https://www.jd.com/')
        dr.maximize_window()
        sleep(2)

        dr.find_element_by_xpath('//*[@id="key"]').send_keys('罗技鼠标')
        sleep(2)

        dr.find_element_by_xpath('/html/body/div[1]/div[3]/div/div[2]/div/div[2]/button').click()
        sleep(2)

        dr.find_element_by_xpath('//*[@id="J_goodsList"]/ul/li[1]/div/div[1]/a/img').click()
        sleep(2)

        wd = dr.window_handles
        dr.switch_to.window(wd[-1])
        sleep(2)

        dr.find_element_by_xpath('//*[@id="InitCartUrl"]').click()
        sleep(2)


        a=dr.title
        dr.assertEqual(a,'商品已成功加入购物车')

        print("添加成功")

if __name__ == '__main__':
    unittest.main()








