from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains#控制鼠标移动的模块
import re
dr=webdriver.Chrome()
dr.get('http://192.168.0.254')
sleep(2)

dr.find_element_by_xpath('/html/body/table/tbody/tr/td/div/form/ul/li[2]/input').send_keys('Bane@7766')
wd=dr.find_element_by_xpath('//*[@id="checkinfo"]').find_elements_by_class_name('nobody')
for i in wd:
    c=i.get_attribute('src')
    dr.find_element_by_xpath('//*[@id="input1"]').send_keys(c[-5])

sleep(2)


dr.find_element_by_xpath('//*[@id="userLoginBox"]/form/ul/li[4]/input[1]').click()
sleep(2)


#弹出框（alert）
wd=dr.switch_to_alert()   #切换到弹出框
print(wd.text)  #获取弹出框的内容
wd.accept()   #点击确定


dr.switch_to.frame('left')
dr.find_element_by_xpath('//*[@id="04"]/span[2]').click()
sleep(2)
dr.find_element_by_xpath('//*[@id="041"]/span').click()
dr.switch_to_default_content()
dr.switch_to.frame('mainFrame')
sleep(5)
dr.find_element_by_xpath('//*[@id="content"]/form[2]/table/tbody/tr/td[2]/div/div/a').click()
sleep(2)
dr.find_element_by_xpath('/html/body/form/table[2]/tbody/tr/td/div/div[1]/a').click()
sleep(5)








# wd.dismiss() #点击取消
#
# wd.send_keys('内容')   #向弹出框输入内容



#dr.quit()