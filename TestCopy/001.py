#coding=utf-8
__author__ = 'zgd'
import unittest

class Test(unittest.TestCase):
    def setUp(self):
        print(u"开始")

    def tearDown(self):
        print(u"结束")

    def test01(self):
        print "执行测试用例 01"

    def test03(self):
        print "执行测试用例 03"

    def test02(self):
        print "执行测试用例 02"

if __name__=='__main__':
    unittest.main()




