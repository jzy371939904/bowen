from selenium import webdriver
from time import sleep
#保证所有的测试用例在同一环境下测试

dr=webdriver.Firefox()#打开浏览器
dr.get('http://www.alltuu.com/') #请求的网址
sleep(2)
#获取网站的标题（title）
print(dr.title)  #通常做断言
#获取网站的网址
print(dr.current_url)

dr.get('http://www.alltuu.com/login?url=http://www.alltuu.com/v')



#通过id属性定位id=kw位置
# dr.find_element_by_id('kw').send_keys('美女')
# sleep(5)
# dr.find_element_by_id('su').click()  #点击的操作
# sleep(5)

#通过class属性定位 定位到
# dr.find_element_by_class_name('s_ipt').send_keys('北京')
# sleep(5)
# dr.find_element_by_id('su').click()
# sleep(5)

#通过name属性定位

dr.find_element_by_id('loginUsername').send_keys('15837806865')
sleep(2)
dr.find_element_by_id('main').click()
sleep(1)
dr.find_element_by_id('loginPassword').send_keys('15837806865')

sleep(2)
dr.find_element_by_id('main').click()
sleep(2)
dr.find_element_by_id('login').click()
sleep(3)


dr.find_element_by_class_name('vToHonePage-nav-header-right-userNick-selectArr').click()

#设置浏览器的大小
dr.set_window_size(400,400)
sleep(2)
#设置浏览器的位置
dr.set_window_position(500,500)
sleep(5)



# dr.maximize_window() #浏览器最大化
# sleep(5)
#
# dr.minimize_window() #浏览器最小化
# sleep(5)


dr.get('https://www.jd.com')
dr.back()#返回上一个网页
sleep(4)
dr.forward()#前进
sleep(2)






dr.quit()  #关闭浏览器