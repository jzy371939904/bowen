#/usr/bin/env python
#-*- conding：'utf-8'
import requests
import unittest
import HTMLTestRunnertest
import time
import re
from 摩尔精英测试框架.config.登陆 import 登陆
from 摩尔精英测试框架.data.数据 import duqu
from 摩尔精英测试框架.test.账号设置 import 更改设置




def baogao(aa):

    suit=unittest.TestSuite()
    for a in aa:
        disvover=unittest.defaultTestLoader.discover(r'..\test',pattern='{}.py'.format(a.strip()))
        suit.addTest(disvover)
        now=time.strftime('%Y %m %d %H-%M-%S',time.localtime(time.time()))
        f=open('abc111.html','wb')

        runner=HTMLTestRunnertest.HTMLTestRunner(tester='焦朝阳',
                                                     description='测试结果如下',
                                                     title='好分数测试报告',
                                                     stream=f,
                                                     )
    runner.run(suit)
    f.close()


