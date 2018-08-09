#coding=utf-8
__author__ = 'zgd'
from Commonlib.Commonlib import Commonlib

class Bussniss():
    def __init__(self):
        self.p = Commonlib()

    def login(self,username,password):
        '''定义登陆函数'''
        # self.p.Login("http://10.248.26.37/ESOP/Login/login.do","tdr","Cmcc@121122")
        self.p.impLicitly(30)
        self.p.openBrowser("http://10.248.26.37/ESOP/Login/login.do")
        self.p.waite(1)
        self.p.clearKeys(".//*[@id='username']")
        self.p.waite(1)
        self.p.inputKeys(".//*[@id='username']",username)
        self.p.waite(1)
        self.p.clearKeys(".//*[@id='password']")
        self.p.waite(1)
        self.p.inputKeys(".//*[@id='password']",password)
        self.p.waite(1)
        self.p.activeEvent(u"//*[contains(text(),'忘记密码')]/preceding-sibling::input[2]")
        self.p.tryFindIframe("iframe_ID_201")
        gt = self.p.getText(u".//*[@id='changePWDText']")
        self.p.waite(1)
        # print(gt)
        return gt

#
# p = Bussniss()
# p.login("tdr","Cmcc@121122")
























































































