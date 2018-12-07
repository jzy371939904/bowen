from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains#控制鼠标移动的模块

#保证所有的测试用例在同一环境下测试

# dr=webdriver.Firefox()#打开浏览器
# dr.get('https://www.jd.com/') #请求的网址
# sleep(2)
# #获取网站的标题（title）
# print(dr.title)  #通常做断言
# #获取网站的网址
# print(dr.current_url)

#通过link——text文本定位

# dr.find_element_by_link_text('企业').click()
# sleep(4)

#partial_link_text 通过文本来定位  模糊查询
# dr.find_element_by_partial_link_text('登').click()
# sleep(5)

#通过标签名称去定位（用于多个元素的定位）

#通过xpath路径定位
#xpath：路径标记语言   他是在xml找东西的    xml：可扩展标记语言
# 1 xml跟html内容是一样的
# 2 xml主要作用：传输数据
# 3 html作用：显示数据
# 1  / 绝对路径
# 2  // 相对路径
# dr.find_element_by_xpath('/html/body/div[2]/div/div[1]/div/div[1]/div[2]/div/span[1]/a').click()
# dr.find_element_by_xpath('//*[@id="user-nomal"]/div[3]/div[1]/li[1]/a')

#通过css定位
#dr.find_element_by_css_selector('')

#定位多个元素 定位多个class属性值的元素
# wd=dr.find_elements_by_class_name('cate_menu_item')
# #print(len(wd))
# for i in wd:
#     ActionChains(dr).move_to_element(i).perform()
#     sleep(2)

#层级定位
# wd=dr.find_element_by_xpath('//*[@id="J_cate"]/ul').find_elements_by_tag_name('li')
# print(len(wd))
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












#移动滚动条   属于浏览器的   javaScript语句
#1根据页面的高度来移动滚动条
# js='var q=document.documentElement.scrollTop=10000'# 控制滚动条的代码
# #10000表示的是当前页面的高度
# dr.execute_script(js)    #执行javascript语句的

#2根据定位到的元素  移动滚动条

# wd=dr.find_element_by_xpath('/html/body/div[1]/div[4]/div[5]/a/div')
# js='arguments[0].scrollIntoView();'
# dr.execute_script(js,wd)





sleep(5)

# dr.find_element_by_xpath('//*[@id="kw"]').send_keys('163')
# sleep(2)
# dr.find_element_by_xpath('//*[@id="su"]').click()
# sleep(2)
# dr.find_element_by_xpath('//*[@id="1"]/h3/a[1]').click()
# sleep(2)
# wd=dr.window_handles
# dr.switch_to_window(wd[1])
# wd=dr.find_element_by_xpath('//*[@id="normalLoginTab"]')
# dr.switch_to_frame(wd)
# sleep(2)
# dr.find_element_by_xpath('//*[@id="auto-id-1543041591694"]').send_keys(15837806865)
# sleep(5)

#获取网站的标题（title）
# print(dr.title)  #通常做断言
# #获取网站的网址
# print(dr.current_url)


# wd=dr.find_element_by_xpath('//*[@id="user-nomal"]/div[3]/div[1]/li[1]/a').text
# print(wd)
# sleep(2)

# for i in wd:
#     i.get_attribute()  #获取元素某一个属性的值

#dr.get('http://www.alltuu.com/login?url=http://www.alltuu.com/v')


dr.quit()

