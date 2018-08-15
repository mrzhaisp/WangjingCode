#coding=utf-8
__author__ = 'zgd'
import re
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import unittest
class TESTLOG(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass

    def test002(self):
        self.assertRegexpMatches('181419235680', r"^(13\d|14[5|7]|15\d|166|17[3|6|7]|18\d)\d{8}$")

    def test001(self):
        self.assertEquals('zhangsa','zhangsa')

if __name__=="__main__":
    unittest.main()

















