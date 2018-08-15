#coding=utf-8
__author__ = 'zgd'
from Bussniss.Bussniss import Bussniss
import unittest
from Commonlib.Readxml import Readxml
r = Readxml()

class Login(unittest.TestCase):
    def setUp(self):
        self.b=Bussniss()
        self.b.p.openBrowser("http://10.248.26.37/ESOP/Login/login.do")

    def tearDown(self):
        self.b.p.closeBrowser()

    def test001(self):
        u'''测试登录是否正常'''
        self.assertEquals(self.b.login(
                r.readxml("login","username"),

                r.readxml("login","password")) ,

                r.readxml("login","epxect")
        )

if __name__=="__main__":
    unittest.main()






































































