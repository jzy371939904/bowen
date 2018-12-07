import requests
import unittest
from 输入地址框架接口.data.输入地址要的数据 import 读取
from 输入地址框架接口.config.地址输入_接口 import 地址输入


class 地址1(unittest.TestCase):
    sss=地址输入().地址_快查
    shuju=读取()
    def test_1(self):
        html=self.tes_学校(self.shuju[0][0])
        self.assertEqual(html['code'],int(self.shuju[0][1]))


    def test_2(self):
        html = self.tes_学校(self.shuju[1][0])
        self.assertEqual(html['code'], int(self.shuju[1][1]))



    def test_3(self):
        html = self.tes_学校(self.shuju[2][0])
        self.assertEqual(html['code'], int(self.shuju[2][1]))

    def test_4(self):
        html = self.tes_学校(self.shuju[0][0])
        self.assertEqual(html['code'], int(self.shuju[0][1]))