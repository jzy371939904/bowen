import xlrd


#登陆的网站
def duqu():
    shuju = []
    f = xlrd.open_workbook('shuju.xls')
    sheet = f.sheets()[0]
    num = sheet.nrows
    for i in range(1,1):
        aaa = sheet.row_values(i)
        shuju.append(aaa)
    return shuju
