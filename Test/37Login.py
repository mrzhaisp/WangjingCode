#coding=utf-8
__author__ = 'zgd'
from Bussniss.Bussniss import Bussniss
from Commonlib.Readxml import Readxml
import unittest
r = Readxml()
class loGin(unittest.TestCase):
    """验证登陆"""
    def setUp(self):
        self.b = Bussniss()
        # self.b.p.openBrowser("http://10.248.26.37/ESOP/Login/login.do")
        # self.verificationErrors=[]

    def tearDown(self):
        self.b.p.closeBrowser()
        # self.assertEqual([],self.verificationErrors)


    def test001(self):
        u"""是否登陆成功"""
        # self.assertEquals(self.b.login("tdr","Cmcc@121122"),u"修改密码")
        self.assertEquals((1+1),3)
if __name__=="__main__":
    unittest.main()































