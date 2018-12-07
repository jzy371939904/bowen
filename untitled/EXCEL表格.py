import xlwt
import xlrd
import xlutils
from xlutils.copy import copy
# #给excel表格写入数据
# f=xlwt.Workbook(encoding='utf-8')
# sheet=f.add_sheet('mingzi ')
# sheet.write(0,0,'姓名')
# f.save('text666.xls')

# #读取数据
# f=xlrd.open_workbook('text666.xls')
# sheet=f.nsheets
# print(sheet)
# sheet=f.sheets()[0]
# print(sheet.nrows)
# a=sheet.nrows
# for i in range(a):
#     print(sheet.row_values(i))

#追加表字段

f=xlrd.open_workbook('text666.xls')
new_f=copy(f)
sheet=new_f.get_sheet(0)
sheet.write(5,5,'小珍珍')
new_f.save('text666.xls')





