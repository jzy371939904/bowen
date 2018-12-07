#！/usr/bin/env python
# -*- coding:utf-8 -*-
import xlwt
import xlrd
import xlutils
# f=xlwt.Workbook(encoding="utf-8") #打开一个空白文件，utf-8在最开头写的时候可以不写
# sheet=f.add_sheet('jzy1')#添加一个标签页，空格里写的是标签页的名称
# sheet.write(0,0,"小珍珍")
# f.save('text1.xls')#保存文件

# f=xlrd.open_workbook('text1.xls') #打开text1这个excle表格
# sheet=f.nsheets  #查看有多少个标签页
# print(sheet)    #显示标签页的个数
# sheet=f.sheets()[0] #通过索引使用想用的标签页
# print(sheet.nrows) #获取文件有多行
# print(sheet.row_values(0)) #读取指定行的内容，0的话就是读取第一行

f=xlrd.open_workbook('text1.xls')#    打开一个excle文件
sheet=f.nsheets    # 获取这个文件的所有标签页
sheet=f.sheets()[0]   #使用一个标签
print(sheet.nrows)    #显示多少行
print(sheet.ncols)    #显示多少列
a=sheet.nrows        #读取文件有多少行
for i in range(a):     #无限循环，并且打印出来
    print(sheet.row_values(i))
#
# import xlrd
# from xlutils.copy import  copy
# f=xlrd.open_workbook('text1.xls') #打开要追加的表格
# new_f=copy(f) #复制一个新的表格
# sheet=new_f.get_sheet(0)  #通过索引打开对应的表
# sheet.write(6,10,'我爱小珍珍')  #舒服位置和要输入的内容
# new_f.save('text1.xls') #保存到表格中
