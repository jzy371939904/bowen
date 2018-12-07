#/usr/bin/env python
# -*- coding:utf-8 -*-
import random
# 输出 等同于在echo  格式：print（）
#print("带空格  试验成功 ")
#print(1231313123)

#输入  从键盘上输入等同与  read -p 提示  变量名     input（提示）
#变量名 = input("请输入成绩：")
#print(变量名)


#变量   变化的量   常量
#定义变量的格式  变量名 = 数据
#多变量
#变量名的明明规则 1.只能是字母，数字，下划线组成
             # 2.不能以数字开头
             # 3.不能命名为函数名
#a,b,c=123,444,555
#print(a,b,c)


#数据类型  str（字符串）  int（整数） float（浮点数） list（列表）
 #       tuple（元组）  dict(字典）  bool（布尔值） none（空值）
 #       set(集合)

# 整数 int  定义整数
#  python自带的函数
#  自己写的函数：自定义函数
# 第一个内置函数：type（） 查看数据类型
#a = 789
#print(type(b))


#a=1.2
#a=float(33.2)
#print(type(a))




#布尔值 bool True  false
#空值  None  是一个特殊的值
#print(type(a))

# str 字符串  一串字符的集合   定义: 字符串
#特点：1不可变的  2 支持索引  反索引  3支持切片
#a='asdfjlsa555jflkajflajfa'
#print(a[::2]) #第一个数字代表起始位置，第二个数字代表结束位置
             # 冒号在后面：从起始开始到最后
             # 冒号在前：从开始到数字代表的位置结束

#属于  字符串的内置函数（对字符串的操作）  局部变量（只适用于字符串）
#调用函数方法：  变量名.函数名（）
#
#a = 'JZY123JZYJJJ'
# b = a.lower()    #将字符串中所有大写变成小写
# # print(b)
# # print(a)
# qqq = 'qqqjzy111 '
# b = qqq.endswith('j')  # 判断字符串是否以括号中的元素结尾
# print(b)
# #print(qqq)

# top = 'hello %s,你孩子今年应该%d岁了'# {} 占位符
# b = top%('小红',222)   #格式化字符串      填充占位符
# print(b)
#

# j = 'a，b，c'
# b = j.split('b')  #以指定字符串为分隔符，将j中的元素分割成一个列表
# print(b)
# print(type(b))

#list（列表）：一组数据的集合 = shell数组
#以中括号为标识，以逗号隔开【元素1，元素2，元素3】
#特点：1.可变的 2支持索引  3支持切片
#作用：用来储存数据
# a=[2,'qwe',25,['sadfasdf','wedw',123],234,111]
# print(a[3][1][-2])

#列表中的内置函数
# a=[2,'qwewqe',2,54]
# #a.append(10) # append 将括号中的元素添加到列表中，注意  只能添加一个
#
# #a.insert(1,'abc') # 第一个参数是下标位置，第二个参数是添加的元素
# a.remove('qwewqe') #  删除某个元素 存在多个一样删除最左边的
# a.pop(0)          # 删除下表位置所在的元素
# print(a)


# a = [2, 'aaa', 2, 54]
# c=a.index(2)   #获取某元素的下标值
# print(c)
# import copy
# b = [4,7,999,232]
# a = [1,'qewr',555,44,b]
# a.extend(b) # 将b列表中的所有元素添加到a列表中
# print(a)
# list


# tuple(元组)  一组数据的集合，都是用来存储数据的
#以小括号为标识，以逗号隔开
#特点  1 不可变的  2支持索引  3 支持切片
# a = (12,1212,433,'qwer')
# a.count(12)   #统计某元素在元组中有多少个
# a.index(1212) #获取某元素的下标位置
# print((type(a)))

#dict（字典）  存储数据的，数据格式： key=value
#以键值对的方式储存数据
#以大括号为标识，以逗号隔开
#特点1 可变的的  2 无序的  3 不支持索引
# a = {'name':'小明','age':'20','sex':'男'}
#
# print(a['age'])

#set（集合）   一组数据的集合，储存数据
#大括号来标识的， 以逗号分隔开 例如｛1，2，3，4，54｝
#特点：1不重复的  2 无序的  3不支持索引  4可变的
# a = {12,234,444,12,345,222,111}
# a.pop()   #随即删除最后一个
# a.remove(12)  #删除括号中的元素
# print(a)

#9*9乘法表
# for i in range(1,10):
#     for j in range(1,i+1):
#         print('%s*%s=%s'%(j,i,i*j),end='\t')
#     print()


# a=[]
# b=''
# c={}  # 空字典
# d=set() #空集合
# 、



# a=[123,321,123,1,2,3,1,1,4,4,555,666,44]
# b=set(a)
# a=list(a)
# a.sort()
# print(a)
# enumerate

#enumerate  函数
#将下标位置和元素对应（字符串，列表，元组）
# a=['asdf','asdfd','qweqwe']
# for i in enumerate(a):
#     print(i)


# a=['电脑','计算机','买瓶水','mp3']
# for i,j in enumerate(a):
#     print(i+1,j)
# b=input('请输入你想要的商品编号')
# b=int(b)
# print(a[b-1])




# 循环嵌套   循环语句中的嵌套其他语句 （判断语句，循环语句）
#循环嵌套判断  for 语句中 if 语句
# for a in range (1,11):
#     if a > 5:
#        print(a)

# b=0
# for a in range(1,100):
#     if a % 2 == 0:
#         b -= a
#     else:
#         b += a
# print(b)

# a = random.randrange(1,10)# 从1-10中随即产生一个数
# a=(input)('输入一个数')
#
# print(a)

#循环嵌套循环  for。。。for。。。
#大循环循环一次，小循环循环一轮
# for i in range(2):
#     for j in range(2):
#         for k in range(4):
#             print(666)
# for i in range(1,10):
#     for j in range (1,i+1):
#         print('{}*{}={}'.format(j,j,i*j),end='\t')
#     print()

# #continue  结束本次循环  break 结束循环
# for i in range(2,7):
#     if i ==5:
#         continue
#     else:
#         print(i)



#for.......else...语句
#原理  只要循环没有被break掉，就执行else下面的语句
# a= ['4ss','1111','efwefwv']
# for i in a:
#     if len(i) == 2:
#         break
# else:
#     print('完美')
# a = random.randint(1,10)
# for i in range(3):
#     b=int(input("请输入你猜的数字："))
#     if b < a:
#         print('猜小了')
#         print("还有{}次机会".format(2-i))
#     elif b > a:
#         print('猜大了')
#         print("还有{}次机会".format(2 - i))
#     elif b == a:
#         print('猜对了，666')
#         break
# else:
#     print('笨蛋')
# a=0
# b=0
# for i  in  range(2,101):
#     for j  in range (2,i+1):
#         a=i%j
#         if a==0:
#             break
#         if j == i:
#             b =b+i
#             print(b)
#



#之和
# !/usr/bin/python
# -*- coding: UTF-8 -*-
# a=0
# b=0
# for i in range(2,101):
#     for j in range (2,i+1):
#         a=i%j
#         if a==0:
#             break


#
#
# #!/usr/bin/python
# # -*- coding: utf-8 -*-
# a=int(input('输入一个数：')):
# s=0
# n=0
# for i in range (1,a)
#

# a=[3,6,9,1,2,2,3,3,4,4,5,5,6]
# b=[]
# for i in a:
#     if i not in b:
#         b.append(i)
#         sort(b)
# print(b)

#while 循环   格式 while 条件：
                    #执行语句
# #打印三次hell world

#for通常用于循环有序列的数据
#while通常用于根据条件循环
#while True：无限循环


# a=0
# b=0
# while a<=100:
#     b += a
#     a += 1
# print(b)
#
# a = random.randint(1,10)
# while True:
#     b=int(input("请输入你猜的数字："))
#     if b < a:
#         print('猜小了')
#     elif b > a:
#         print('猜大了')
#     elif b == a:
#         print('猜对了，666')
#         break


#while 循环的嵌套  嵌套判断语句，循环语句
# while True:
#     while True:
#         for i in range(10):
#             if i == 9:
#                 break
#             else:
#                 print(i)
#         break
#     break
#
# a=1
# while a<10:
#     b = 1
#     while b<=a:
#         print('%s*%s=%s'%(a,b,a*b),end='\t')
#         b+=1
#     print
#     a+=1

#while ....else...语句
#循环只要不被break掉，就执行else语句
# a=0
# while a<3:
#     print('hello ')
#     a+=1
#     break
# else:
#     print(123)

# a=0
# for i in range (2,101):
#     for j in range(2,i):
#         if i%j==0:
#             break
#     else:
#         a+=i
# print(a)

# a=[6,6,6,64]
# b=sum(a)
# print(b/4)
#
# a=input("输入")
# b=a.split(',')
# sum=0
# for i in b:
#     sum+=int(i)
# print(sum/len(b))
# for

# a=input("输入字符串")
# if a.startswith("a"):
#     if a.endswith("b"):
#         print("ok")
# else:
#         print("no")



# a=['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
# b=1000
# f=''
# while True:
#     c=b%16
#     b=b//16
#     f+=a[c]
#     if b==0:
#         break
# print(f[::-1])


# a='asdfdsa'
# b=len(a)//2
# for i in range(b):
#     if a[i] != a[-i-1]:
#         print('no')
#         break
# else:
#     print('yes')
#
# a='1233321'
# b=(a[::-1])
# for i in range(len(b)):
#     if a[i] != a[-i-1]:
#         print('no')
#         break
# else:
#     print('yes')
# #
# a=[1,1,2,3,3,4,55,666]
# b=a.index(max(a))
# c=a.index(min(a))
#
# a[b],a[0]=a[0],a[b]
# a[c],a[-1]=a[-1],a[c]
# print(a)


# a=input('输入三角形三边：')
# a=a.split(',')
# a[0]=int(a[0])
# a[1]=int(a[1])
# a[2]=int(a[2])
# a.sort()
# if a[0]+a[1]>a[2]:
#     if a[0]**2+a[1]**2==a[2]**2:
#         print('直角')
#     elif a[0]**2+a[1]**2<a[2]**2:
#         print('钝角')
#     elif a[0]**2+a[1]**2>a[2]**2:
#         print('锐角')
# else:
#     print('啥都不是')




# 函数  具有某种功能，可重复使用的代码块
#   格式     定义函数
#          def  函数名（）：
#                执行语句
#函数名的规则和变量名的规则一样
# def jj():
#     for i in range(1,10):
#         for j in range (1,i+1):
#             print('%s*%s=%s'%(i,j,j*i),end=('\t'))
#         print()
# qqq=jj()
# qqq
# jj()

#函数的传参   1必须参数
#   格式     定义函数
#          def  函数名（变量名）：
#                执行语句
# def jj(x,y):
#     for i in range(x,y):
#         for j in range (1,i+1):
#             print('%s*%s=%s'%(i,j,j*i),end=('\t'))
#         print()
# jj(3,6)



#函数的传参   2默认参数
#   格式     定义函数
#          def  函数名（变量名）：
#                执行语句
# def jj(x=4):
#     for i in range(1,x):
#         for j in range (1,i+1):
#             print('%s*%s=%s'%(i,j,j*i),end=('\t'))
#         print()
# jj

#函数的传参   3可变长参数
#   格式     定义函数
#          def  函数名（*参数）：
#                执行语句        默认args是可变长参数
# def jj(*args):
#     for i in range(1,args[0]):
#         for j in range (1,i+1):
#             print('%s*%s=%s'%(i,j,j*i),end=('\t'))
#         print()
# jj(7)

#    **kwargs   接收到只能是键值对
# def aaa(**kwargs):
#     print(kwargs)
#
# aaa(ddd=111,des=111)


# for i in range (0,10,2):
#     print(i)


# def  jzy1(x):
#      a=[x]
#      b=[]
#      for i in a:
#          if i not in b:
#             b.append(i)
# print(a)




#变量的作用域
# a=123    # 在函数外的变量属于全局变量
# def aaa():
#     a=99999 #函数中的变量属于局部变量
#     print(a)
# aaa()
# print(a)



#return  1函数的结束语  2将结果返回给调用者
# def aaa():
#     a=0
#     for i in range(2,101):
#         for j in range(2,i):
#             if i%j==0:
#                 break
#         else:
#             a+=i
#     print(a)
#     return a
# print(aaa()+1)\\

#lambda   匿名函数  用来定义函数的、
#格式  ：  函数名 = lambda:表达式

# aa=lambda x,y : x + y
# bb=lambda x,y : x - y
# cc=lambda x,y : x * y
# dd=lambda x,y : x // y
# a=input('>>>>')
# a=a.split(',')
# if '+' in a:
#     print(aa(int(a[0],int(a[2])))
# elif '-' in a:
#     print(bb(int(a[0],int(a[2])))
# elif '*' in a:
#     print(cc(int(a[0],int(a[2])))
# elif '//' in a:
#     print(dd(int(a[0],int(a[2])))
# else:
#     print('失败')
#计算器，两个数之间的加减乘除


#列表推导式 将依据放在列表中，产生的结果变成列表的元素
# c=[]
# for i in range(10):
#     if i>5:
#       c.append(i)
#
# b=[str(x*2) for x in range(10) if x>5]
#
# print(c)
# print(b)




# a=(12,55,32,1,542)
# print(max(a))  #最大值
# print(min(a))  #最小值

#
# a=100
# print(hex(a))    #将十进制转换十六进制
# print(oct(a))    #将十进制转换八进制
# print(bin(a))    #将十进制转换二进制
# # print(int(a))    #将其他进制转换为十进制
#
# a,b=divmod(100,16) #整除求余
#  print(a,b)


# for i in range(10):
#     s=0
#     for j in range(1,i):
#         if i%j==0:
#             s+=j
#     if s==i:
#         print(i)
#会文字符串
# a='123123222'
# b=(a[::-1])
# for i in range(len(b)):
#     if a[1] != a[-i-1]:
#         print('no')
#         break
# else:
#     print('yes')


# #1-100之和
# a=0
# for i in range(1,101):
#     a+=i
# print(a)

#三次猜数字 无限循环
# a=random.randint(1,10)
# while True:
#     b=int(input('输入你要猜的数字'))
#     if b>a:
#             print('大了')
#     if b<a:
#             print('小了')
#     if b==a:
#             print('对了')
#             break

# a=input(">>>>>>>")
# b=a.split(",")
# c=[]
# for i,j in enumerate(b):
#     b[i]=int(j)
# for c in b:
#     for e in b:
#         for f in b:
#             if (c!=e) and (c!=f) and (e!=f):
#                 h=(e*100+f*10+k)
#                 print(h)


#水仙花数
# for i in range(100,1000):
#     a=i//100
#     b=i//10%10
#     c=i%10
#     if a**3+b**3+c**3==i:
#         print(i)


# a=[123,11,233,4,12,51,1231,2,2,2,6666,66666]
# b=a.split()
# c=[]
# for i in enumerate(b):

# a=input('输入')
# if a.startswith('a'):
#     if a.endswith('c'):
#         print('是a开头c结尾')
#     else:
#         print('不是')
# elif a.endswith('c'):
#     print('是c结尾')
# else:
#     print('啥都不是')


# a=input(">>>>>")
# a=a.split(',')
# b=a.copy()
# b.sort()
# print(b))
# a=input('>')
# b=a.split(',')
# for i,j in enumerate(b):
#     b[i]=int(j)
# b.max             #  这一行sort了，可以不
# f=b.copy()
# c=b[-1]
# for d in f:
#     if d==c:
#         print(d)
# for i in f:
#     if d==c:
#         f.remove(c)
# c=f[-1]
# for e in f:
#     if e==c:
#         print(e)
# def tt():
#     for i in range(1,5):
#         for j in range(1,5):
#          for k in range(1,5):
#              if i!=j and j!=k and k!=i:
#                     print(i,j,k)
# tt()
# a=input('>>>>>')
# a=list(set(a.sort()))
# c,e=b[-1],b[-2]
# f,g=a.count(c),a.count(e)
# print(c*f,e*q)


# a=0
# for i in range(1,101):
#     a+=i
# print(a)

# a=0
# b=(x for x in range(1,101)  a+=x)
# print(a)
# 打开一个空文件
#a.txt 文件名：如果不加路径，表示在当前目录下文件
#如果此目录下有这个文件，就操作这个文件，没有就创建
#如果有路径就在路径上加上双斜杠\\ 表示不转义
#或者在路径引号前面加上小写的r
#对文件的操作  open()  函数
#格式    open('文件名','权限','编码方式')
#权限：代码对文件的操作权限
# w  写的权限---write（“写入的东西”只能是字符串）
# r  读取的权限 f.read（） 读取文件中所有的内容，结构是字符串类型
#             f.readlines（）  读取文件中多有数据类型，结果是列表
#             f.readline（） 读取文件中一行内容，结果是字符串

# f=open(r'C:\Users\jzy\Desktop\a.jpg','rb')
# # a  追加的权限
# #     f.write（）具有不换行功能
# #wb  rb  ab  以字节码的格式读写追加
# print(f.read())
# f.close()


# 上下文管理器   with 语句  原理：——enter——，——exit——
#对文件的打开和关闭强制执行的操作
#格式： with 打开文件   as  变量名：
# with  open('a,txt','r',encoding='utf-8') as f:
#     aa=f.readlines()
# for i in aa:
#     if i =='\n' or i.startswith('#'):
#         aa.remove(i)
# print(len(aa))
#
# import  os
# for i in range(10):#创建十个文件
#     with open('{}.txt'.format(i),'w',encoding='utf-8') as f:
#         for j in range(10):
#             f.write('111111'+'\n')
# for k in range(9):#删除9个文件
#     os.remove('{}.txt'.format(k))


#异常处理语句
#异常：因代码逻辑关系导致的成语中断
#异常处理（捕获）：对将要发生的异常进行预防  try。。except。。。 语句
#格式：  try：
#           执行语句（有可能会发生异常的语句）
#       except：
#           执行语句
#针对某一种异常或多种异常去处理
# try:
#     print(a+1)
# except Exception as x:#默认处理所有的异常
#     print(x)

#try...except....else  只要try语句代码没有异常，就执行else
#try...except...finally...       finally语句一定会被执行
# try:
#     a=(dfsdf)
#     print(a+1)
# except:
#     print(1)
# finally:
#     print('强制执行')

#raise  #触发异常   自定义异常
# a=123
# raise:('我要吃火锅，要吃薯片，要吃双皮奶，你给不给我买')
# print(123+1)

# import qwe  # 库    模块
#
# from qwe import jj  #从qwe文件中导入jj这个函数
# from qwe import *   #从qwe文件中导入所有的函数
# print(jj)
# print()


#面向对象   抽象    将函数进行分类和封装，使开发更高效
#只关注   输入和输出
#在python上是通过 类  来实现某个对象的功能
#定义类：  class 类名（）：
#              def 函数名（）：
#                   执行语句
#              def 函数名（）：
#                   执行语句

#类：属性 ：每一种方法必须具备的条件
#   方法：def

#
# class Shuzi():   #为了跟函数名区分，类名首字母最好是大写，小写也可以
#     def jiujiu(self):      #self 也是类的实例化
#         print('1111')
#     def zhishu(self):
#         print('4444')
# #对象是类的实际化
#实例化：自定义：方便在类的外部调用
#       内置：方便在类的内部调用
# a=Shuzi()
# a.zhishu()

#继承   一个新的类拥有旧的类的所有方法
# class asd(Shuzi):
#     pass   #空语句
#
# asd=asd()
# asd.zhishu()

#object  一切基础的类
#多继承：一个新的类拥有多个旧的类的所有方法
#如果继承的多个类中有相同的方法，使用的是最左边的类里面的
#
# class asd():
#     def __init__(self,a,b):  #初始化属性
#         self.name = a
#         self.nianji = b
#
#     def aaa(self):
#         print('hello %s，今年%d年纪'%(self.name,self.nianji))
#
#     def bbb(self):
#         print('hello %s，今年还没娶到媳妇' % (self.name))
# aa=asd('阿金',411)
# aa.aaa()
# aa.bbb()

#多态    方法重写  :多用于版本升级
#私有方法   只属于本类的方法
#定义私有方法：在方面名的前面加上 两个下划线 __

#常用的模块的使用 1 pymysql  对Mysql数据库操作
# import pymysql
# # 连接数据库
# abc=pymysql.connect(host='192.168.0.156',
#                     port=3306,
#                     user='root',
#                     password='123456',
#                     charset='utf8')
#  # 创建游标
# aaa = abc.cursor()
#
# # aaa.execute('show databases;')   #执行sql语句
# #
# # print(aaa.fetchall())  #读取上一句sql语句的结果(元组 )
# # aaa.execute('use arlicle;')
# # aaa.execute('show tables;')
# # aaa.execute('select * from fxs;')
# # # print(aaa.fetchmany(4))  #读取指定条数的数据
# # # print(aaa.fetchall())    #剩下的数据会被fetchall读取
# # print(aaa.fetchone())    #每次读取一个结果，本身有迭代的功能
# # print(aaa.fetchone())
# # print(aaa.fetchone())
# # print(aaa.fetchone())
#
#
# # aaa.execute('create database jjj;')
# aaa.execute('use jjj;')
# # aaa.execute('create table jzy1(姓名 char(30),年龄 int,班级 char(10));')
# # list1 = ['小张',1,'软件测试少儿班']
# # for i in range(30):
# #     aaa.execute('insert into jzy1 values("{}","{}","{}");'.format(list1[0],list1[1]+i,list1[2]))
# #     abc.commit() # 提交数据
# # for i in aaa.fetchall():
# #     print(i)
# aaa.execute('select * from jzy1;')
# sj=aaa.fetchall()
# aaa.execute('desc jzy1')
# bt=aaa.fetchall()
# with open('ass.txt','w',encoding='utf-8') as f:
#     # for i in range(len(bt)):
#     #     if i == len(bt)-1:
#     #         f.write(bt[i][0])
#     #     else:
#     #         f.write(bt[i][0]+',')
#     for j in sj:
#         f.write('\n'+'{},{},{}'.format(j[0],j[1],j[2]))


#os模块  python自带的模块
#作用：python与操作系统之间的交互
import os
# a=os.popen('nslookup www.taobao.com')   #popen执行windows命令
# print(a.read())
#print(os.getcwd())  #获取当前所在的位置

# 切换目录
#os.chdir(r'C:\Users\jzy\PycharmProjects\untitled')

#创建目录
#os.mkdir('54321')  #如果不加路径就在当前目录下创建

#创建递归目录
#os.makedirs(r'54321\12345\11111')

#删除递归目录
#os.removedirs(r'54321\12345\11111')

#删除文件
# os.remove('1i.txt')

#删除空目录
#os.rmdir('aaaa')

#获取当前目录下的所有文件
#print(os.listdir(r'C:/Users/jzy'))

#更改文件名
#os.rename('3666.txt','2.txt')

#将文件名和路径分隔开
# 分割的字符串与有无此文件或路径无关

#将文件的后缀名与路径分隔开
#print(os.path.splitext(r'C:/Users/jzy/PycharmProjects/untitled/jzy.py'))

#os.path.isfile(‘文件名’) #判断是否为普通文件
#os.path.isdir(‘文件名’) 判断是否为目录文件
#os.path.islink('文件名') 判断是否为链接文件
# a=0
# b=0
# c=0
# os.chdir(r'E:\qq')
# for i in os.listdir():
#     if os.path.isfile(i):
#         a+=1
#         print(a)
#     if os.path.isdir(i):
#         print(i)
#     if os.path.islink(i):
#         print(i)

# os.chdir(r'E:\qq')
# a=[i for i in os.listdir() if os.path.isfile(i)]
# b=[j for j in os.listdir() if os.path.isdir(j)]
# print(len(a))
# print(len(b))



# xlwt 需要下载的木块 作用;给excel表格写入数据
# xlrd            作用   读取excel表格中的数据
# xlutils        作用   给excel表格中追加数据
# import xlwt
# import xlrd
# import xlutils
#
# #打开一个空白文件
# f=xlwt.Workbook(encoding='utf-8')
# #添加一个标签页，括号中写标签页的名称
# sheet=f.add_sheet("python操作excel")
# #写入数据
# #第一个数字代表多少行，第一行从0开始
# #第二个数字代表多少列，第一列从0开始
# #第三个内容里面输入想要输入的内容
# sheet.write(0,0,'姓名')
# sheet.write(0,1,'年龄')
# sheet.write(0,2,'班级')
# a=['小明',11,'包婚配']
# for i in range(30):
#     sheet.write(i+1,0,a[0])
#     sheet.write(i+1,1,a[1])
#     sheet.write(i+1,2,a[2])
# #保存文件
# f.save('text.xls')

# import xlrd   #读取excel表格
#
# #打开一个文件
# f=xlrd.open_workbook('text.xls')

#两种获取标签页  1通过索引来获取
# sheet=f.nsheets  #获取有多少个标签页
# print(sheet)
# sheet=f.sheets()[0]  #索引获取标签页
#
# print(sheet.nrows)#获取文件有多少行
#
# print(sheet.row_values(0))  #row_values()读取第几行内容，从第一行从零开始
#
# a=sheet.nrows  #读取文件有多少行
# for i in range(a):
#     print(sheet.row_values(i))  #读取本页所有的内容
#
# print(sheet.ncols)    #获取有多少列
# print(sheet.col_values(0))   #读取第几列的内容，第一列从零开始
#
# print(sheet.cell(2,3).value)  #读取某一个单元格的内容

#2.通过标签页的名称
# print(f.sheet_names())  #获取所有标签页的名称
#
# sheet=f.sheet_by_name('python操作excel')  #括号中填写操作的标签页


#excel表格的追加
# import xlrd
# from xlutils.copy  import copy
#
# f=xlrd.open_workbook('text.xls')
#
# #复制一份文件
# new_f=copy(f)
#
# # 操作复制的文件
# sheet=new_f.get_sheet(0)  #通过索引来获取
#
# sheet.write(5,10,'小珍珍真丑') #在指定行列插入文字
#
# new_f.save('text.xls')


#封装了ssh协议  作用：远程连接
# import paramiko
#
# #创建一个ssh客户端
# ssh111=paramiko.SSHClient()
#
# #把将要连接的主机添加到 know_hosts 文件中
# ssh111.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#
# ssh111.connect(hostname='192.168.0.164',
#                port=22,
#                username='root',
#                password='111111')
#执行命令
# stuin,stuout,stuerr=ssh111.exec_command('ls -al')
# #第一个变量：执行的命令，输入
# #第二个变量：命令的结构，输出
# #第三个变量：命令的报错
# print(stuout.read().decode())
#
# ssh111.close() # 断开命令

# while True:
#     a=input("输入命令,退出输入exit:")
#     if a=='exit':
#         break
#     else:
#         stuin, stuout, stuerr = ssh111.exec_command(a)
#         print(stuout.read().decode())
# ssh111.close()


#
# import  paramiko
#
# #创建一个传输通道   接收的只能是元祖
# ssh111=paramiko.Transport(('192.168.0.164',22))
# ssh111.connect(username='root',password='111111')
#
# #传输文件使用sftp协议，  创建一个sftp实例
# sftp=paramiko.SFTPClient.from_transport(ssh111)
#
# #get是从linux下载文件到本地
# sftp.get('anaconda-ks.cfg','./aaa.cfg')
#
# #put是从本地向linux上传文件
# sftp.put('qwe.py','/etc/aaa.py')
#
# sftp.close()



#发送邮件

import smtplib #发动邮件的协议
import email.mime.text#处理发送的内容
import email.mime.multipart#处理邮件的表头

sender='m15837806865@163.com'#发送者
recver='15037109541@163.com'#接收者
server='smtp.163.com'#  服务器地址
passwd='jzy123456'          #授权码

#创建一个空邮件
message=email.mime.multipart.MIMEMultipart()

#发件人
message['from']= sender

#收件人
message['to']= recver

#主题
message['subject']='python 错误报告'

#正文
text='''
我是小川镇
我是小珍珍
我是真传销
我是传销真
'''


#处理文本信息
text=email.mime.text.MIMEText(text)

#将处理后的信息添加到邮件里
message.attach(text)

#定义服务器和端口
smtp111=smtplib.SMTP_SSL(server,465)

#登陆服务器
smtp111.login(sender,passwd)

#发送邮件
smtp111.sendmail(sender,recver,message.as_string())

#断开连接
smtp111.close()

