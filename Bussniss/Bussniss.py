#coding=utf-8
__author__ = 'zgd'
from Commonlib.Commonlib import Commonlib
from Commonlib.MysqlClient import MysqlClient

import time
import re
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
class Bussniss():
    def __init__(self):
        self.p = Commonlib()
        self.m = MysqlClient()
    def login(self,username,password):
        '''定义登陆函数'''
        # self.p.Login("http://10.248.26.37/ESOP/Login/login.do","tdr","Cmcc@121122")
        # self.p.openBrowser("http://10.248.26.37/ESOP/Login/login.do")
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
        gml = self.p.tryText(u".//span[text()='客户服务']").encode("utf-8")
        return gml
        # if  gml == u'客户服务':
        #     print(u"成功")
        # else:
        #     print(u"失败")
# p = Bussniss()
# p.login("tdr","Cmcc@121122")

    def pooderShenpi(self,username,password):
        u"""验证审批人"""
        # self.p.openBrowser("http://10.248.26.37/ESOP/Login/login.do")
        # self.p.waite(1)
        self.p.clearKeys(".//*[@id='username']")
        self.p.waite(1)
        self.p.inputKeys(".//*[@id='username']",username)
        self.p.waite(1)
        self.p.clearKeys(".//*[@id='password']")
        self.p.waite(1)
        self.p.inputKeys(".//*[@id='password']",password)
        self.p.waite(1)
        self.p.activeEvent(u"//*[contains(text(),'忘记密码')]/preceding-sibling::input[2]")
        self.p.tryTimesleep("iframe_ID_201")
        self.p.tryMoveLocation(u".//span[text()='超时工单提醒']")
        self.p.waite(2)
        self.p.activeEvent( u".//*[@id='menuDiv']/descendant::div[text()='网络资源勘查']")
        self.p.waite(2)
        self.p.shiFangFrame()
        self.p.waite(1)
        self.p.tryTimesleep("iframe_ID_20321")
        self.p.tryFindToclick(".//*[@id='btnCustomerSelect-btnEl']")
        self.p.trySendKeys(".//*[@id='keyWord']/descendant::input", u"99回归")
        self.p.waite(1)
        self.p.activeEvent( u".//span[text()='查 询']/parent::button")
        self.p.waite(1)
        self.p.activeEvent( u".//div[contains(text(),'99回归87')]")
        self.p.waite(1)
        self.p.activeEvent( u".//span[text()='确定']/parent::button")
        self.p.waite(1)
        self.p.inputKeys( u".//*[contains(text(),'产品名称')]/following-sibling::div[1]/input", u"数据专线2.0")
        self.p.waite(1)
        self.p.tryFindToclick(u".//li[contains(text(),'数据专线2.0')]")
        self.p.waite(1)
        self.p.activeEvent( ".//*[@id='vipGrid-body']/descendant::td[5]/div")
        self.p.waite(1)
        self.p.activeEvent( ".//*[@id='vipGrid-body']/div[2]/descendant::div[4]")
        self.p.waite(1)
        self.p.activeEvent( ".//*[@id='vipGrid-body']/descendant::td[6]/div")
        self.p.waite(1)
        self.p.inputKeys( ".//*[@id='vipGrid-body']/div[3]/descendant::input", "Mbit/s")
        self.p.waite(1)
        self.p.activeEvent( ".//*[@id='vipGrid-body']/descendant::td[7]/div")
        self.p.waite(1)
        self.p.inputKeys(".//*[@id='vipGrid-body']/div[4]/descendant::input", u"普通级")
        self.p.waite(1)
        self.p.activeEvent( ".//*[@id='vipGrid-body']/descendant::td[10]/div")
        self.p.waite(1)
        self.p.inputKeys( ".//*[@id='vipGrid-body']/div[5]/descendant::input", u"北京")
        self.p.waite(1)
        self.p.activeEvent( ".//*[@id='vipGrid-body']/descendant::td[11]/div")
        self.p.waite(1)
        self.p.inputKeys( ".//*[@id='vipGrid-body']/div[6]/descendant::input", u"北京")
        self.p.waite(1)
        self.p.activeEvent( ".//*[@id='vipGrid-body']/descendant::td[12]/div")
        self.p.waite(1)
        self.p.inputKeys( ".//*[@id='vipGrid-body']/div[7]/descendant::input", u"西城区")
        self.p.waite(1)
        self.p.activeEvent( ".//*[@id='vipGrid-body']/descendant::td[13]/div")
        self.p.waite(1)
        self.p.inputKeys( ".//*[@id='vipGrid-body']/div[8]/descendant::input", u"西城区西区")
        self.p.waite(1)
        self.p.activeEvent( ".//*[@id='vipGrid-body']/descendant::td[14]/div")
        self.p.waite(2)
        self.p.inputKeys( ".//*[@id='vipGrid-body']/div[9]/descendant::input", u"其他")
        self.p.waite(2)
        self.p.jsLeft()
        self.p.waite(1)
        self.p.activeEvent( ".//*[@id='vipGrid-body']/descendant::td[17]/div")
        self.p.waite(1)
        self.p.inputKeys( ".//*[@id='vipGrid-body']/div[10]/descendant::input", u"A端张三")
        self.p.waite(1)
        self.p.activeEvent( ".//*[@id='vipGrid-body']/descendant::td[18]/div")
        self.p.waite(1)
        self.p.inputKeys( ".//*[@id='vipGrid-body']/div[11]/descendant::input", u"150889821321")
        self.p.waite(1)
        self.p.activeEvent( ".//*[@id='vipGrid-body']/descendant::td[19]/div")
        self.p.waite(1)
        self.p.inputKeys( ".//*[@id='vipGrid-body']/div[12]/descendant::input", u"liling1")
        self.p.waite(1)
        self.p.activeEvent( ".//*[@id='vipGrid-body']/descendant::td[20]/div")
        self.p.waite(1)
        self.p.inputKeys( ".//*[@id='vipGrid-body']/div[13]/descendant::input", u"1803293829")
        self.p.waite(1)
        self.p.jsLeft()
        self.p.waite(1)
        self.p.activeEvent( ".//*[@id='vipGrid-body']/descendant::td[22]/div")
        self.p.waite(1)
        self.p.inputKeys( ".//*[@id='vipGrid-body']/div[14]/descendant::input", u"广东")
        self.p.waite(3)
        self.p.activeEvent( ".//*[@id='vipGrid-body']/descendant::td[23]/div")
        self.p.waite(3)
        self.p.inputKeys( ".//*[@id='vipGrid-body']/div[15]/descendant::input", u"佛山")
        self.p.waite(3)
        self.p.activeEvent( ".//*[@id='vipGrid-body']/descendant::td[24]/div")
        self.p.waite(3)
        self.p.inputKeys( ".//*[@id='vipGrid-body']/div[16]/descendant::input", u"三水区")
        self.p.waite(1)
        self.p.activeEvent( ".//*[@id='vipGrid-body']/descendant::td[25]/div")
        self.p.waite(1)
        self.p.inputKeys( ".//*[@id='vipGrid-body']/div[17]/descendant::input", u"三水区详细")
        self.p.waite(1)
        self.p.activeEvent( ".//*[@id='vipGrid-body']/descendant::td[26]/div")
        self.p.waite(1)
        self.p.inputKeys( ".//*[@id='vipGrid-body']/div[18]/descendant::input", u"其他")
        self.p.waite(2)
        self.p.jsLeft1900()
        self.p.waite(3)
        self.p.activeEvent( ".//*[@id='vipGrid-body']/descendant::td[29]/div")
        self.p.waite(3)
        self.p.inputKeys( ".//*[@id='vipGrid-body']/div[19]/descendant::input", u"z端联系人")
        self.p.waite(3)
        self.p.activeEvent( ".//*[@id='vipGrid-body']/descendant::td[30]/div")
        self.p.waite(3)
        self.p.inputKeys( ".//*[@id='vipGrid-body']/div[20]/descendant::input", "18652635265")
        self.p.waite(1)
        self.p.activeEvent( u".//*[text()='Z端客户经理姓名']")
        self.p.tryMoveLocation(u".//*[contains(text(),'产品联系人电话')]")
        self.p.activeEvent( ".//*[@id='submitButton-btnEl']")
        self.p.waite(2)
        self.p.activeEvent(u".//*[contains(text(),'送下一环节')]/following-sibling::div[1]/div[2]/div")
        gmxl = self.p.tryText(u".//*[contains(text(),'送专线勘察和调度管')]").encode("utf-8")
        # print(gmxl)
        return gmxl

# p = Bussniss()
# p.getPooder("tdr","Cmcc@121122")
    def getPoorder(self,username,password):
        u'''poordernumber'''
        # self.p.openBrowser("http://10.248.26.37/ESOP/Login/login.do")
        # self.p.waite(1)
        self.p.clearKeys(".//*[@id='username']")
        self.p.waite(1)
        self.p.inputKeys(".//*[@id='username']",username)
        self.p.waite(1)
        self.p.clearKeys(".//*[@id='password']")
        self.p.waite(1)
        self.p.inputKeys(".//*[@id='password']",password)
        self.p.waite(1)
        self.p.activeEvent(u"//*[contains(text(),'忘记密码')]/preceding-sibling::input[2]")
        self.p.tryTimesleep("iframe_ID_201")
        self.p.tryMoveLocation(u".//span[text()='超时工单提醒']")
        self.p.waite(2)
        self.p.activeEvent( u".//*[@id='menuDiv']/descendant::div[text()='网络资源勘查']")
        self.p.waite(2)
        self.p.shiFangFrame()
        self.p.waite(1)
        self.p.tryTimesleep("iframe_ID_20321")
        self.p.tryFindToclick(".//*[@id='btnCustomerSelect-btnEl']")
        self.p.trySendKeys(".//*[@id='keyWord']/descendant::input", u"99回归")
        self.p.waite(1)
        self.p.activeEvent( u".//span[text()='查 询']/parent::button")
        self.p.waite(1)
        self.p.activeEvent( u".//div[contains(text(),'99回归87')]")
        self.p.waite(1)
        self.p.activeEvent( u".//span[text()='确定']/parent::button")
        self.p.waite(1.5)
        self.p.inputKeys( u".//*[contains(text(),'产品名称')]/following-sibling::div[1]/input", u"数据专线2.0")
        self.p.waite(1.5)
        self.p.tryFindToclick(u".//li[contains(text(),'数据专线2.0')]")
        self.p.waite(1.5)
        self.p.activeEvent( ".//*[@id='vipGrid-body']/descendant::td[5]/div")
        self.p.waite(1.5)
        self.p.activeEvent( ".//*[@id='vipGrid-body']/div[2]/descendant::div[4]")
        self.p.waite(1.5)
        self.p.activeEvent( ".//*[@id='vipGrid-body']/descendant::td[6]/div")
        self.p.waite(1.5)
        self.p.inputKeys( ".//*[@id='vipGrid-body']/div[3]/descendant::input", "Mbit/s")
        self.p.waite(1.5)
        self.p.activeEvent( ".//*[@id='vipGrid-body']/descendant::td[7]/div")
        self.p.waite(1.5)
        self.p.inputKeys(".//*[@id='vipGrid-body']/div[4]/descendant::input", u"普通级")
        self.p.waite(1.5)
        self.p.activeEvent( ".//*[@id='vipGrid-body']/descendant::td[10]/div")
        self.p.waite(3)
        self.p.inputKeys( ".//*[@id='vipGrid-body']/div[5]/descendant::input", u"北京")
        self.p.waite(1.5)
        self.p.activeEvent( ".//*[@id='vipGrid-body']/descendant::td[11]/div")
        self.p.waite(3)
        self.p.inputKeys( ".//*[@id='vipGrid-body']/div[6]/descendant::input", u"北京")
        self.p.waite(2)
        self.p.activeEvent( ".//*[@id='vipGrid-body']/descendant::td[12]/div")
        self.p.waite(3)
        self.p.inputKeys( ".//*[@id='vipGrid-body']/div[7]/descendant::input", u"西城区")
        self.p.waite(3)
        self.p.activeEvent( ".//*[@id='vipGrid-body']/descendant::td[13]/div")
        self.p.waite(3)
        self.p.inputKeys( ".//*[@id='vipGrid-body']/div[8]/descendant::input", u"西城区西区")
        self.p.waite(1)
        self.p.activeEvent( ".//*[@id='vipGrid-body']/descendant::td[14]/div")
        self.p.waite(2)
        self.p.inputKeys( ".//*[@id='vipGrid-body']/div[9]/descendant::input", u"其他")
        self.p.waite(2)
        self.p.jsLeft()
        self.p.waite(1.5)
        self.p.activeEvent( ".//*[@id='vipGrid-body']/descendant::td[17]/div")
        self.p.waite(1.5)
        self.p.inputKeys( ".//*[@id='vipGrid-body']/div[10]/descendant::input", u"A端张三")
        self.p.waite(1)
        self.p.activeEvent( ".//*[@id='vipGrid-body']/descendant::td[18]/div")
        self.p.waite(1)
        self.p.inputKeys( ".//*[@id='vipGrid-body']/div[11]/descendant::input", u"150889821321")
        self.p.waite(1)
        self.p.activeEvent( ".//*[@id='vipGrid-body']/descendant::td[19]/div")
        self.p.waite(1)
        self.p.inputKeys( ".//*[@id='vipGrid-body']/div[12]/descendant::input", u"liling1")
        self.p.waite(1)
        self.p.activeEvent( ".//*[@id='vipGrid-body']/descendant::td[20]/div")
        self.p.waite(1)
        self.p.inputKeys( ".//*[@id='vipGrid-body']/div[13]/descendant::input", u"1803293829")
        self.p.waite(1)
        self.p.jsLeft()
        self.p.waite(1)
        self.p.activeEvent( ".//*[@id='vipGrid-body']/descendant::td[22]/div")
        self.p.waite(1)
        self.p.inputKeys( ".//*[@id='vipGrid-body']/div[14]/descendant::input", u"广东")
        self.p.waite(2)
        self.p.activeEvent( ".//*[@id='vipGrid-body']/descendant::td[23]/div")
        self.p.waite(3)
        self.p.inputKeys( ".//*[@id='vipGrid-body']/div[15]/descendant::input", u"佛山")
        self.p.waite(3)
        self.p.activeEvent( ".//*[@id='vipGrid-body']/descendant::td[24]/div")
        self.p.waite(3)
        self.p.inputKeys( ".//*[@id='vipGrid-body']/div[16]/descendant::input", u"三水区")
        self.p.waite(3)
        self.p.activeEvent( ".//*[@id='vipGrid-body']/descendant::td[25]/div")
        self.p.waite(3)
        self.p.inputKeys( ".//*[@id='vipGrid-body']/div[17]/descendant::input", u"三水区详细")
        self.p.waite(2)
        self.p.activeEvent( ".//*[@id='vipGrid-body']/descendant::td[26]/div")
        self.p.waite(2)
        self.p.inputKeys( ".//*[@id='vipGrid-body']/div[18]/descendant::input", u"其他")
        self.p.waite(2)
        self.p.jsLeft1900()
        self.p.waite(1)
        self.p.activeEvent( ".//*[@id='vipGrid-body']/descendant::td[29]/div")
        self.p.waite(1)
        self.p.inputKeys( ".//*[@id='vipGrid-body']/div[19]/descendant::input", u"z端联系人")
        self.p.waite(1)
        self.p.activeEvent( ".//*[@id='vipGrid-body']/descendant::td[30]/div")
        self.p.waite(3)
        self.p.inputKeys( ".//*[@id='vipGrid-body']/div[20]/descendant::input", "18652635265")
        self.p.waite(3)
        self.p.activeEvent( u".//*[text()='Z端客户经理姓名']")
        self.p.waite(3)
        self.p.tryMoveLocation(u".//*[contains(text(),'产品联系人电话')]")
        self.p.activeEvent( ".//*[@id='submitButton-btnEl']")
        self.p.waite(5)
        self.p.activeEvent(u".//*[contains(text(),'送下一环节')]/following-sibling::div[1]/div[2]/div")
        self.p.waite(5)
        self.p.tryFindToclick(u".//*[contains(text(),'送下一环节')]/ancestor::div[5]/following-sibling::div[1]/descendant::span[text()='确定']/parent::button")
        self.p.waite(2)
        poorderInfo = self.p.tryText(u".//span[contains(text(),'提交成功')]")
        # print(poorderInfo)
        poorderInfo1 = re.split(':',poorderInfo)
        poorDerNumBer = poorderInfo1[-1]
        tag = 'ocdzykc'
        creaTeDate = time.strftime("%Y-%m-%d %H:%M:%S")
        with open('../DataShare/zykc-ordernumbs.txt','r') as f:
            f.write(poorDerNumBer + '    ')
            f.write(creaTeDate + '    ')
            f.write(tag + '\n')
        # muMs = [].extend(poorDerNumBer,creaTeDate ,tag)
        # nuMs = []
        # nuMs.insert(0,poorDerNumBer)
        # nuMs.insert(1,creaTeDate)
        # nuMs.insert(2,tag)
        # print(nuMs,'------------')
        # self.m.dateAdd(nuMs)
        # print("*"*30,poorDerNumBer)
        return poorDerNumBer


# #
# p = Bussniss()
# p.getPoorder("tdr","Cmcc@121122")


# 0001808156555437












































































