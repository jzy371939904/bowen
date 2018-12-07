from appium import webdriver
import  time


#启动设备，链接设备



desired_caps={'platformName':'Android',
              #'platformVersion':'6.2',
              'deviceName':'127.0.0.1:62026',
              'appPackage':'com.netease.cloudmusic',
              'appActivity':'activity.LoadingActivity'}

driver=webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)


print('立即体验')
driver.find_element_by_id('com.netease.cloudmusic:id/mw').click()
time.sleep(3)
driver.find_element_by_id('com.netease.cloudmusic:id/pt').click()
time.sleep(5)
driver.find_element_by_id('com.netease.cloudmusic:id/i4').send_keys(15837806865)
time.sleep(5)
driver.find_element_by_id('com.netease.cloudmusic:id/i2').send_keys(15837806865)
time.sleep(5)
driver.find_element_by_id('com.netease.cloudmusic:id/pt').click()
time.sleep(5)
driver.find_element_by_id('com.netease.cloudmusic:id/py').click()
time.sleep(5)
driver.find_element_by_id('com.netease.cloudmusic:id/b3t').click()
time.sleep(5)