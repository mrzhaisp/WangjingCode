#coding=utf-8
__author__ = 'zgd'
from Bussniss.Bussniss import Bussniss
from Commonlib.Readxml import Readxml
import unittest
r = Readxml()

class PoorderShenpi(unittest.TestCase):
    def setUp(self):
        self.b = Bussniss()
        self.b.p.openBrowser("http://10.248.26.37/ESOP/Login/login.do")

    def tearDown(self):
        self.b.p.closeBrowser()

    def test001(self):
        '''测试username为tdr时审批人是否正常'''
        self.assertEquals(self.b.getPooder(
                r.readxml("shenpi","username"),

                r.readxml("shenpi","password")) ,

                r.readxml("shenpi","epxect")
        )
if __name__=="__main__":
    unittest.main()











































