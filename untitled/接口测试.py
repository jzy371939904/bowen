#/usr/bin/env python
#-*- conding：'utf-8'


#接口测试：发送请求   验证响应是否符合需求的过程
#postman     jmeter


#requests 发送http请求   assert 断言处理

import requests
import unittest  #是python自带的单元测试框架
#1  unittest TestCase   用例的管理：主要是管理用例的
#2  unittest TestSuite  测试套件：多个测试用例集合在一起
#3  unittest Tsetloader  测试载入：将测试用例加载到测试套件中
#4  unittest TestRunner  执行测试用例
#    封装了检验返回的结果
class xuexiao1(unittest.TestCase):  #学校1继承这个unittest。TestCase
    def setUp(self):   #初始化测试环境  每次执行测试用例前执行
        print('初始化成功')

    def tearDown(self):  #清理环境：每次用例执行之后去执行
        print('清理成功')

    def test_1(self):   #以test开头的测试用例  必须以test开头
        url = 'http://testsupport-be.haofenshu.com/v1/schools/infos'
        a =input('>>>>>>>')
        querystring = {'filterInput': '{}'.format(a)}
        head = {
            'cookie': 'yz-test-session-id=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJvcGVyYXRvciI6ImxpeGlhbndlaSIsInJvbGVUeXBlIjoxLCJpYXQiOjE1MzkwNTgxOTYsImV4cCI6MTU3MDU5NDE5Nn0.GzWTsN7Sb9W85R1Wem8_HNV7e8oXTQSCPdvODb5f_GA'
        }
        re = requests.get(url=url, headers=head, params=querystring)
        html = re.json()
        # print(html)
        assert html['code'] == 0
        print('成功')


    def test_2(self):
        url = 'http://testsupport-be.haofenshu.com/v1/schools/infos'
        a ='55555'
        querystring = {'filterInput': '{}'.format(a)}
        head = {
            'cookie': 'yz-test-session-id=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJvcGVyYXRvciI6ImxpeGlhbndlaSIsInJvbGVUeXBlIjoxLCJpYXQiOjE1MzkwNTgxOTYsImV4cCI6MTU3MDU5NDE5Nn0.GzWTsN7Sb9W85R1Wem8_HNV7e8oXTQSCPdvODb5f_GA'
        }
        re = requests.get(url=url, headers=head, params=querystring)
        html = re.json()
        # print(html)
        assert html['code'] != 0
        print('失败')

unittest.main()





# class xuexiao():
#     def aaa(self,a):
#         url='http://testsupport-be.haofenshu.com/v1/schools/infos'
#         a=input('>>>>>')
#         querystring={'filterInput':'{}'.format(a)}
#         head={
#             'cookie':'yz-test-session-id=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJvcGVyYXRvciI6ImxpeGlhbndlaSIsInJvbGVUeXBlIjoxLCJpYXQiOjE1MzkwNTgxOTYsImV4cCI6MTU3MDU5NDE5Nn0.GzWTsN7Sb9W85R1Wem8_HNV7e8oXTQSCPdvODb5f_GA'
#         }
#         re=requests.get(url=url,headers=head,params=querystring)
#         html=re.json()
#         #print(html)
#
#         #自带的断言
#         assert html['code']==0   #判断预期的结果是否与断言的结果一致
#




