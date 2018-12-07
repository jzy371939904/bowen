import xlrd


def duqu():
    shuju = []
    f = xlrd.open_workbook('qweqwe.xls')
    sheet = f.sheets()[0]
    num = sheet.nrows
    for i in range(1, num):
        aaa = sheet.row_values(i)
        shuju.append(aaa)
    return shuju
