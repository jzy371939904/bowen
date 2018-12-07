import xlrd

shuju = []
f = xlrd.open_workbook('666.xlsx')
sheet = f.sheets()[0]
num = sheet.nrows
for i in range(1, num):
    aaa = sheet.row_values(i)
    shuju.append(aaa)
print(shuju)
