#时间模块

import time

# #时间戳   代表公元1970年到现在经过的  秒数
# print(time.time())
#
# #本地时间   元组  默认显示的是当前时间
# #参数：是填写时间戳
# print(time.localtime())
#
# #格式化成现代化时间
# print(time.strftime('%Y %m %d %H-%M-%S %w',time.localtime()))
#将现代化时间格式化成元组
#print(time.strptime('1999 12 12','%Y %m %d'))


#将元组的时间转换为时间戳
# a=(1999,12,12,12,23,33,2,1,0)#按照前六个算，但是要写九个不然报错
# print(time.mktime(a))

#休眠
# time.sleep(7)
# print(666)

# a=int(input('输入一个时间;'))
# if a%4==0:
#     if a%100==0:
#         if a%400==0:
#             print('{}是闰年'.format(a))
#         else:
#             print('{}不是闰年'.format(a))
#     else:
#         print('{}不是闰年'.format(a))
# elis:
#     print('{}不是闰年'.format(a))


# a = input("请输入一个年月日：")
# b=a.split(',')
# if (int(b[0]) % 4 == 0 and int(b[0]) % 100) != 0 or int(b[0]) % 400 == 0:
#     print("{}是闰年".format(b[0]))
# else:
#     print("{}不是闰年".format(b[0]))
# c=time.strptime('{} {} {}'.format(b[0],b[1],b[2]),'%Y %m %d')
# print('今天是周{}'.format(c[-3]+1))
# print('今天是一年地{}天'.format(c[-2]))



a=input('>>>输入一个年月日')
b=a.split(',')
c=time.strptime('{} {} {}'.format(b[0],b[1],b[2]),'%Y %m %d')
print(c)
d=int(time.mktime(c)-864000)
print(time.localtime(d))