from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains#控制鼠标移动的模块

dr=webdriver.Firefox()
dr.get('https://www.baidu.com')#打开要登录的页面
sleep(2)
dr.find_element_by_xpath('//*[@id="kw"]').send_keys('开封大学')
sleep(2)
dr.find_element_by_xpath('//*[@id="su"]').click()
sleep(2)
dr.find_element_by_xpath('//*[@id="1"]/h3/a[1]/em').click()
sleep(2)
wd=dr.window_handles
dr.switch_to_window(wd[1])
dr.find_element_by_xpath('/html/body/div[5]/div[1]/div[2]/div[2]/div[2]/div[2]/a[4]').click()
sleep(2)
wd=dr.window_handles
dr.switch_to_window(wd[2])
dr.find_element_by_xpath('/html/body/div[3]/div[2]/div[2]/div[2]/div/dl[1]/dt[1]/a').click()
sleep(2)
wd=dr.window_handles
dr.switch_to_window(wd[3])
dr.find_element_by_xpath('//*[@id="txt_asmcdefsddsd"]').send_keys(2015481270)
sleep(2)



dr.quit()