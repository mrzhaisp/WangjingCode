#coding=utf-8
__author__ = 'zgd'
from Commonlib.Commonlib import Commonlib
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
class BussinessShenPi():
    def __init__(self):
        self.p = Commonlib()

    def shenPi(self,username,password):
        self.p.openBrowser("http://10.248.26.37/ESOP/Login/login.do")
        self.p.waite(1)
        self.p.clearKeys(".//*[@id='username']")
        self.p.waite(1)
        self.p.inputKeys(".//*[@id='username']", username)
        self.p.waite(1)
        self.p.clearKeys(".//*[@id='password']")
        self.p.waite(1)
        self.p.inputKeys(".//*[@id='password']", password)
        self.p.waite(1)
        self.p.activeEvent(u"//*[contains(text(),'忘记密码')]/preceding-sibling::input[2]")
        self.p.tryTimesleep("iframe_ID_201")
s = BussinessShenPi()
s.shenPi("bazhiwei","Cmcc@121122")














































