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
        self.p.tryTimesleep("iframe_ID_301")
        self.p.tryFindToclick(u".//*[contains(text(),'产品名称')]/ancestor::div[5]/following-sibling::div/descendant::tbody/descendant::td[3]/descendant::a")
        self.p.shiFangFrame()
        self.p.tryFindIframe("iframe_ID_waitWork")
        self.p.impLicitly(30)
        self.p.tryMoveLocation(u".//*[contains(text(),'请审批')]")
        self.p.tryMoveLocation(u".//*[contains(text(),'下一办理步骤')]")
        self.p.inputKeys(u".//*[contains(text(),'处理意见')]/parent::div/div[1]/textarea",u"已批准")
        self.p.activeEvent(".//*[@id='nextArg-bodyEl']/div[2]/div[1]")
        self.p.tryMoveLocation(u".//*[contains(text(),'下一办理步骤')]")
        gttm = self.p.getText(u".//*[contains(text(),'补录专线属性')]")
        print(gttm)
        self.p.activeEvent(u".//*[contains(text(),'补录专线属性')]")
        self.p.activeEvent(".//*[@id='nextNode-btnEl']")
        self.p.activeEvent(".//*[text()='Yes']/parent::button")
        self.p.alterAccept()
ss = BussinessShenPi()
ss.shenPi("bazhiwei","Cmcc@121122")














































