#/usr/bin/env python
#-*- conding：'utf-8'

import requests
import unittest
from 摩尔精英测试框架.config.登陆 import 登陆
from 摩尔精英测试框架.data.数据 import duqu
from 摩尔精英测试框架.test.账号设置 import 更改设置
from 摩尔精英测试框架.report.摩尔经营报告 import baogao

import HTMLTestRunnertest
import time
import re






class Test_run():
#生成测试报告     生成一个测试套件
    def run_多个(self,aa):
        baogao(aa)
    def run_all(self,aa):#跑所有
        baogao(aa)


if __name__=='__main__':
    run=Test_run()
    with open('run.txt','r')as f:#打开txt文件，判断文件执行的是多个还是所有
        aa=f.readlines()
        print(aa)
        if 'all' in aa:
            aa=['test*']
            run.run_all(aa)
        else:
            run.run_多个(aa)