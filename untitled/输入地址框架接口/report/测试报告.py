#/usr/bin/env python
#-*- conding：'utf-8'


import requests
import unittest
from 输入地址框架接口.data.输入地址要的数据 import 读取
from 输入地址框架接口.config.地址输入_接口 import 地址输入
from 输入地址框架接口.test.测试1 import 地址1
import HTMLTestRunnertest
import time
import re


def baogao(aa):

    suit=unittest.TestSuite()
    for a in aa:
        disvover=unittest.defaultTestLoader.discover(r'..\test',pattern='{}.py'.format(a.strip()))
        suit.addTest(disvover)
        now=time.strftime('%Y %m %d %H-%M-%S',time.localtime(time.time()))
        f=open('abc.html','wb')

        runner=HTMLTestRunnertest.HTMLTestRunner(tester='焦朝阳',
                                                     description='测试结果如下',
                                                     title='好分数测试报告',
                                                     stream=f,
                                                     )
    runner.run(suit)
    f.close()