#/usr/bin/env python
#-*- conding：'utf-8'

import requests
import unittest
from 框架.config.学校_接口 import 学校_查询
from 框架.data.读取数据的 import duqu
from 框架.test.test666 import 学校1
from 框架.report.测试报告 import baogao
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







        # 测试类 = []
        # with open('run.txt', 'r')as f:
        #     aaa = f.read()
        #     aaa = aaa.split('\n')
        #     for i in aaa:
        #         f = open(r'..\ttest111\{}.py'.format(i), 'r', encoding='utf-8')
        #         a = f.read()
        #         b = re.compile(r'class (.*?):', re.S)
        #         c = b.findall(a)
        #         for j in c:
        #             jjj = j.split('(')
        #             print(jjj[0])
        #             o = globals()['{}'.format(jjj[0])]
        #             print(o)
        #             测试类.append(o)



