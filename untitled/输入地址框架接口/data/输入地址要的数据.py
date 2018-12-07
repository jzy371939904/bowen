import xlrd



def 读取():
    shuju=[]
    f=xlrd.open_workbook('123.xls')
    sheet=f.sheets()[0]
    num = sheet.nrows
    for i in range(1, num):
        aaa = sheet.row_values(i)
        shuju.append(aaa)
    return shuju





