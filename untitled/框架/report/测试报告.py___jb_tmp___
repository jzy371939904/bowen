#/usr/bin/env python
#-*- conding：'utf-8'

import requests
import unittest
from 框架.config.学校_接口 import 学校_查询
from 框架.data.读取数据的 import duqu
from 框架.test.test666 import 学校1
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
