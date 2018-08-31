#coding=utf-8
__author__ = 'Administrator'
from Commonlib.Commonlib import Commonlib
class tetsAlter():
    def __init__(self):
        self.b = Commonlib()

    def altertable(self):
        self.b.openBrowser("C:\\Users\\Administrator\\Desktop\\alter.html")
        # self.b.activeEvent(".//*[@id='alert']")
        self.b.activeEvent(".//*[@id='confirm']")
        # self.b.activeEvent(".//*[@id='prompt']")

        self.b.waite(2)
        self.b.dissMissAlter()
        print(u'准备关闭浏览器')
        self.b.quitBrowser()
mm = tetsAlter()
mm.altertable()













