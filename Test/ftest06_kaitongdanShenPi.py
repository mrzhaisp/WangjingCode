#coding=utf-8
__author__ = 'zgd'
from Bussniss.Bussniss import Bussniss
from Commonlib.Readxml import Readxml
import unittest
r = Readxml()

class KaitongDanShenPi(unittest.TestCase):

    def setUp(self):
        self.b = Bussniss()

    def tearDown(self):
        self.b.p.closeBrowser()

    def test001(self):
        """客户经理提开通单审批人员"""
        self.assertEquals(self.b.kaiTongShenPi(
                            r.readxml("kaitongdanshenpi","username"),
                            r.readxml("kaitongdanshenpi","password")),
                            r.readxml("kaitongdanshenpi","epxect"))

if __name__=="__main__":
    unittest.main()
























