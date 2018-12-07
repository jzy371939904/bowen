import requests
import unittest
from 框架.config.学校_接口 import 学校_查询
from 框架.data.读取数据的 import duqu

class 学校1(unittest.TestCase):
    tes_学校=学校_查询().学校_快查
    shuju=duqu()
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