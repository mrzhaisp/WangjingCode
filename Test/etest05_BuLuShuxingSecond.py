#coding=utf-8
from Bussniss.Bussniss import Bussniss
from Commonlib.Readxml import Readxml
import unittest
r = Readxml()
class buLuShuXingSecond(unittest.TestCase):
    """第二次补录属性验证"""
    def setUp(self):
        self.b = Bussniss()
        # self.b.p.openBrowser("http://10.248.26.37/ESOP/Login/login.do")
    def tearDown(self):
        self.b.p.closeBrowser()

    def test001(self):
        """测试第二次次补录是否成功"""
        self.assertEquals(self.b.buLuShuxingSecond(),
            r.readxml("bulushuxingSecond","epxect")

        )

if __name__=="__main__":
    unittest.main()












