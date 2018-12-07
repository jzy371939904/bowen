
import requests
import unittest
import xlrd

class xuexiao1(unittest.TestCase):
    def setUp(self):      ## 主要的作用：初始化测试环境。    每次执行测试用例前执行
        print('开始')

    def tearDown(self):    ## 清理环境   每次用例执行之后去执行
        print('结束')


    def test_1(self):
        url = 'http://testsupport-be.haofenshu.com/v1/schools/infos'
        f = xlrd.open_workbook(r'‪C:\Users\jzy\Desktop\1.xlsx')
        sheet = f.nsheets
        sheet = f.sheets()[0]
        pp = sheet.col_values(0)
        # print(pp[0])

        for i in pp:
            # print(i)


            querystring = {'filterInput': '{}'.format(i)}

            headers = {
                'cookie': 'yz-test-session-id=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJvcGVyYXRvciI6ImxpeGlhbndlaSIsInJvbGVUeXBlIjoxLCJpYXQiOjE1MzkwNTgxOTYsImV4cCI6MTU3MDU5NDE5Nn0.GzWTsN7Sb9W85R1Wem8_HNV7e8oXTQSCPdvODb5f_GA',
                'Content-Type': 'application/x-www-form-urlencoded'}

            res = requests.get(url=url, headers=headers, params=querystring)
            # print(res.json())
            html = res.json()
            print(html['code'])

    def test_2(self):
        url = 'http://testsupport-be.haofenshu.com/v1/schools/infos'
        f = xlrd.open_workbook(r'‪C:\Users\jzy\Desktop\1.xlsx')
        sheet = f.nsheets
        sheet = f.sheets()[0]
        pp = sheet.col_values(0)
        # print(pp[0])

        for j in pp:
        # print(i)

            querystring = {'filterInput': '{}'.format(j)}

            headers = {
                'cookie': 'yz-test-session-id=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJvcGVyYXRvciI6ImxpeGlhbndlaSIsInJvbGVUeXBlIjoxLCJpYXQiOjE1MzkwNTgxOTYsImV4cCI6MTU3MDU5NDE5Nn0.GzWTsN7Sb9W85R1Wem8_HNV7e8oXTQSCPdvODb5f_GA',
                'Content-Type': 'application/x-www-form-urlencoded'}

            res = requests.get(url=url, headers=headers, params=querystring)
            # print(res.json())
            html = res.json()
            print(html['data'])
#
#
unittest.main()