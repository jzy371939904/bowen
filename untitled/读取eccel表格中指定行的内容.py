import xlrd#读取模块
f=xlrd.open_workbook('text.xls')#打开指定的Excel表格
sheet=f.sheets()[0]#读取第一个下标的表格
print(sheet.nrows)# 当前表格中有多少行
a=sheet.nrows#获取文件中有多少行
for i in range(10,15):#循环10到15行内容
    print(sheet.row_values(i))#打印出来
