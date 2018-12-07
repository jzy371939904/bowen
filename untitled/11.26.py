from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains#控制鼠标移动的模块
import selenium.webdriver.support.ui as ui


dr=webdriver.Firefox()

dr.get('http://www.moore.ren/')
dr.maximize_window()
sleep(2)
#强制等待  例如：sleep（2）



# 智能等待   设置控制器dr等待
un=ui.WebDriverWait(dr,10)
un.until(lambda dr:dr.find_element_by_xpath('//*[@id="user-nomal"]/div[1]/a/img').is_displayed())
#is_displayed 判断元素是否显示在屏幕上
#is_enabled   判断元素是否为灰化状态

print(un)


#截图功能
dr.get_screenshot_as_png()  #截图的函数
dr.save_screenshot('jt.png')#保存截图


#截图并保存
dr.get_screenshot_as_file('jtt.png') #一行代码





dr.quit()



# 1，把字符串变成整数
# a='33333322342'
# b=a[::-1]
# s=0
# for i,j in enumerate(b):
#     for h in range(10):
#         if str(h)==j:
#             s+=h*10**i
# print(s)




# 5、九九乘法表
# for i in range(1,10):
#     for j in range(1,i+1):
#         print('{}*{}={}'.format(i,j,i*j),end='\t')
#     print()






#7、质数之和
# def zhishu(a,b):
#     s=0
#     c=0
#     for i in range(a,b+1):
#         for j in range(2,i+1):
#             c=i%j
#             if c==0:
#                 break
#         if j==i:
#                s=s+i
#     print(s)
#
# zhishu(10,100)





#创建一个目录，创建十个文件，添加十行内容
# import os
# os.chdir(r'C:\Users\zhang\Desktop')
# os.mkdir(r'C:\Users\zhang\Desktop\目录')
# for i in range(10):
#     with open(r'C:\Users\zhang\Desktop\目录\{}.txt'.format(i),'a',encoding='utf-8') as f:
#         for j in range(10):
#             f.write('asdfghjkl'+'\n')
# for m in range(10):
#     os.remove(r'C:\Users\zhang\Desktop\目录\{}.txt'.format(m))
# os.rmdir(r'C:\Users\zhang\Desktop\目录')



#txt到数据库
# import pymysql
# aaa = pymysql.connect(host='192.168.0.76',
#                       port=3306,
#                       user='root',
#                       password='654321',
#                       charset='utf8')
# a=aaa.cursor()
# a.execute('use shujuku;')
# with open('1.txt','r',encoding='utf-8') as f:
#     b = f.readlines()
#     # a.execute('create table biao1(姓名 char(255),年龄 int,学号 int);')
#     for i in b:
#         if i[0]!='姓名':
#             a.execute('insert into biao1 values("{}","{}","{}");').format(i[0],i[1],i[2])
# a.execute('select * from biao1;')
# for i in a.fetchall():
#     print(i)





#爬虫
# import re
# import requests
# class qiushi(object):
#     def qingqiu(self,page):
#         url = 'https://www.qiushibaike.com/8hr/page/{}/'.format(page)
#         head = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}
#         response = requests.get(url=url,headers=head)
#         html = response.content.decode('utf-8')
#         return html
#
#     def guolv(self,abc):
#         shuju=[]
#         patt = re.compile('<div class="content"> (.*?) </div>',re.S)
#         items = patt.findall(abc)
#         for i in items:
#             i=i.replace('<span>','')
#             i=i.replace('</span>','')
#             i=i.strip()
#             shuju.append(i)
#         return shuju
#
#
#     def save(self,shuju):
#         with open('a.txt','a',encoding='utf-8') as f:
#             for i in shuju:
#                 f.write(i+'\n')



# import socket
# s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# host = ('192.168.0.68',2000)
# s.bind(host)
# s.listen(3)
# while True:
#     a,b=s.accept()
#     msg = a.recv(1024)
#     print(msg.decode('utf-8'))
#     reg = 'welcome'
#     a.send(reg.encode('utf-8'))
#
#
#
# import socket
# soc = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# soc.connect(('192.168.0.68',2000))
# aaa = 'hi'
# soc.send(aaa.encode('utf-8'))
# msg = soc.recv(1024)
# print(msg.decode('utf-8'))

