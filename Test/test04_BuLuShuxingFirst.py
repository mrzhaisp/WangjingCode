#coding=utf-8
__author__ = 'zgd'
import sys
import os
sys.path.append(os.getcwd())
from Bussniss.Bussniss import Bussniss
from Commonlib.Readxml import Readxml
import unittest
r = Readxml()
class buLuShuXingOne(unittest.TestCase):
    def setUp(self):
        self.b = Bussniss()
        # self.b.p.openBrowser("http://10.248.26.37/ESOP/Login/login.do")

    def tearDown(self):
        self.b.p.closeBrowser()

    def test001(self):
        """测试首次补录是否成功"""
        self.assertEquals( self.b.buLuShuxingFirst( ),
            r.readxml("bulushuxingOne","epxect")

        )
if __name__=="__main__":
    unittest.main()




















