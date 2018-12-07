import requests
import unittest
import HTMLTestRunne   #生成的是英文的测试报告
import HTMLTestRunnertest   #生成的是中文的测试报告
import time
import xlrd
class xuexiao1(unittest.TestCase):  #学校1继承这个unittest。TestCase
    # def setUp(self):   #初始化测试环境  每次执行测试用例前执行
    #     print('初始化成功')
    #
    # def tearDown(self):  #清理环境：每次用例执行之后去执行
    #     print('清理成功')
    def tes_数据(self):
        shuju=[]
        f=xlrd.open_workbook('666.xls')
        sheet=f.sheets()[0]
        num=sheet.nrows
        for i in range(1,num):
            aaa=sheet.row_values(i)
            shuju.append(aaa)
        return shuju


    def xuexiao(self,a):
        url='http://testsupport-be.haofenshu.com/v1/schools/infos'

        querystring={'filterInput':'{}'.format(a)}
        head={
            'cookie':'yz-test-session-id=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJvcGVyYXRvciI6ImxpeGlhbndlaSIsInJvbGVUeXBlIjoxLCJpYXQiOjE1MzkwNTgxOTYsImV4cCI6MTU3MDU5NDE5Nn0.GzWTsN7Sb9W85R1Wem8_HNV7e8oXTQSCPdvODb5f_GA'
        }
        re=requests.get(url=url,headers=head,params=querystring)
        html=re.json()
        return html
        #print(html)
    def test_1(self):
        shuju=self.tes_数据()
        html=self.xuexiao(shuju[0][0])
        self.assertEqual(html['code'],int(shuju[0][1]))
        # self.assertIn(len(html['data']),range(int(shuju[0][2])))

    def test_2(self):
         shuju = self.tes_数据()
         html=self.xuexiao(shuju[1][0])
         self.assertIn('学校快查成功',html['msg'])
         self.assertEqual(len(html['data']),0)



    def test_3(self):
         shuju = self.tes_数据()
         html = self.xuexiao(shuju[2][0])
         self.assertNotEqual(html['code'],1)

    def test_4(self):
        html = self.xuexiao('111111')
        self.assertEqual(html['code'],1)

if __name__=='__main__':

    #生成测试报告     生成一个测试套件
    suit=unittest.TestSuite()
    #添加测试用例  将测试用例添加到测试套件中
    # suit.addTest(xuexiao1('test_1'))
    # suit.addTest(xuexiao1('test_2'))
    # suit.addTest(xuexiao1('test_3'))
    # suit.addTest(xuexiao1('test_4'))
    suit.addTest(unittest.makeSuite(xuexiao1)) #找到xueixao1中所有测试用例添加到测试套件中
    now=time.strftime('%Y %m %d %H-%M-%S',time.localtime(time.time()))
    f=open('abc.html','wb')

    runner=HTMLTestRunnertest.HTMLTestRunner(tester='焦朝阳',
                                             description='测试结果如下',
                                             title='好分数测试报告',
                                             stream=f,
                                             )
    runner.run(suit)
    f.close()

    # unittest.main()








