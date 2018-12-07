from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains#控制鼠标移动的模块

dr=webdriver.Firefox()
dr.get('https://i.qq.com')#打开要登录的页面
sleep(2)

# dr.find_element_by_xpath('//*[@id="user-nomal"]/div[3]/div[1]/li[1]/a').click()
# sleep(2)
# #print(dr.current_window_handle) #获取当前窗口的句柄
# #print(dr.window_handles) #获取所有窗口的句柄
#
# wd=dr.window_handles
# print(dr.window_handles)
# dr.switch_to_window(wd[-1])   #根据句柄  切换窗口
# dr.find_element_by_xpath('//*[@id="emailInput"]').send_keys(15837806865)
# sleep(2)
# dr.find_element_by_xpath('//*[@id="passwordInput"]').send_keys(15837806865)
# sleep(1)
# dr.find_element_by_xpath('//*[@id="userForm"]/input[1]').click()
# sleep(2)
# #dr.switch_to_window(wd[0])
# dr.find_element_by_xpath('//*[@id="searchform"]/input[1]').send_keys('软件测试工程师')
# dr.find_element_by_xpath('//*[@id="search-submit"]').click()
# sleep(2)

#框架是镶嵌在web（网页）上的一个窗口




wd=dr.find_element_by_xpath('//*[@id="login_frame"]')#复制的是iframe的框架
#切换框架
dr.switch_to.frame(wd)   #切换到内嵌框架中  只能根据：id或name属性的值来定位到框架进行切换
sleep(2)
dr.find_element_by_xpath('//*[@id="switcher_plogin"]').click()
dr.find_element_by_xpath('//*[@id="u"]').send_keys(371939904)
sleep(2)
dr.find_element_by_xpath('//*[@id="p"]').send_keys(964989494)
sleep(2)

dr.switch_to_default_content() #退出到原始的页面
#dr.switch_to.parent_frame()  #切换到上一层框架
#只能根据：id属性的值，name属性的值，定位到框架  来切换
sleep(2)





dr.quit()