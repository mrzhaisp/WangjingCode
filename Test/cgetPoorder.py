#coding=utf-8
__author__ = 'zgd'
import sys
import os
sys.path.append('D:\\WangjingCode\\Commonlib')
sys.path.append('D:\\WangjingCode\\Bussniss')

from Bussniss.Bussniss import Bussniss
from Commonlib.Readxml import Readxml
from Commonlib.MysqlClient import MysqlClient

import unittest
r = Readxml()

import re

class getPoorder(unittest.TestCase):
    def setUp(self):
        self.b = Bussniss()
        self.m = MysqlClient()
        self.b.p.openBrowser("http://10.248.26.37/ESOP/Login/login.do")

    def tearDown(self):
        self.b.m.dateAdd()
        self.b.p.closeBrowser()

    def test001(self):
        u"""是否000开头"""
        self.assertIn(

                r.readxml("poorder", "epxect"),

                self.b.getPoorder(
                #得到poorDerNumBer
                r.readxml("poorder","username"),
                r.readxml("poorder","password"))

        )

        # self.assertRegexpMatches(
        #     # 得到正则表达式子
        #         r.readxml("poorder", "epxect"),
        #
        #         self.b.getPoorder(
        #         #得到poorDerNumBer
        #         r.readxml("poorder","username"),
        #         r.readxml("poorder","password"))
        #
        #
        #
        # )
if __name__=="__main__":
    unittest.main()




















