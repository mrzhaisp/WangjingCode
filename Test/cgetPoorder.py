#coding=utf-8
__author__ = 'zgd'
from Bussniss.Bussniss import Bussniss
from Commonlib.Readxml import Readxml
import unittest
r = Readxml()
import re

class getPoordernumber(unittest.TestCase):
    def setUp(self):
        self.b = Bussniss()
        self.b.p.openBrowser("http://10.248.26.37/ESOP/Login/login.do")

    def tearDown(self):
        self.b.p.closeBrowser()

    def test001(self):
        self.assertRegexpMatches(self.b.getPoorder(
                #得到poorDerNumBer
                r.readxml("poorder","username"),
                r.readxml("poorder","password")) ,

                #得到正则表达式子
                r.readxml("poorder","epxect")

        )
if __name__=="__main__":
    unittest.main()




















