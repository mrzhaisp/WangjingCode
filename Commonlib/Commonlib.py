#coding=utf-8
# __author__ = 'zgd'
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time as t
import sys
import os
sys.path.append(os.getcwd())
class Commonlib():
    def __init__(self):

        """加载firefox配置文件"""
        self.dr = webdriver.Firefox(webdriver.FirefoxProfile("C:\Users\Administrator\AppData\Roaming\Mozilla\Firefox\Profiles\glw65f77.default"))
        # self.dr = webdriver.Firefox()
    def openBrowser(self,myurl):
        """打开浏览器"""
        self.dr.get(myurl)
        self.dr.maximize_window()

    def closeBrowser(self):
        """关闭浏览器"""
        self.dr.close()

    def localElement(self,value):
        """找到元素不做操作"""
        return  self.dr.find_element("xpath",value)

    def activeEvent(self,value):
        """点击事件"""
        self.dr.find_element("xpath",value).click()

    def inputKeys(self,value,sk):
        """输入关键字"""
        self.dr.find_element("xpath",value).send_keys(sk)

    def clearKeys(self,value):
        """清楚输入框内容"""
        self.dr.find_element("xpath",value).clear()

    def waite(self,num):
        """强制等待"""
        t.sleep(num)

    def moveElement(self,value):
        """移动到字符不做操作"""
        gt = self.localElement(value)
        ActionChains(self.dr).move_to_element(gt).perform()

    def tryFindIframe(self,value):
        """循环寻找iframe"""
        for i in range(10):
            try:
                self.dr.switch_to.frame(value)
                break
            except:pass
            t.sleep(1)

    def tryMoveLocation(self,value):
        """循环去找关键字然后"""
        for i in range(10):
            try:
                target = self.dr.find_element("xpath",value)
                self.dr.execute_script("arguments[0].scrollIntoView();", target)
                break
            except:pass
            t.sleep(1)

    def tryFindToclick(self,value):
        """循环去找元素去点击"""
        for i in range(20):
            try:
                self.dr.find_element("xpath",value).click()
                break
            except:pass
            t.sleep(1)
        else:
            print(u"没有找到关键字点击不了")

    def moveTopDown(self):
        """控制滚动条"""
        js = "var q=document.documentElement.scrollTop=300"
        self.dr.execute_script(js)

    def shiFangFrame(self):
        """释放iframe"""
        self.dr.switch_to.default_content()


    def jsLeft(self):
        """处理横向滚动条"""
        jsleft = 'document.getElementsByClassName("x-scroller-ct")[0].scrollLeft=1000'
        self.dr.execute_script(jsleft)

    def jsLeft1900(self):
        """处理横向滚动条"""
        jsleft = 'document.getElementsByClassName("x-scroller-ct")[0].scrollLeft=1900'
        self.dr.execute_script(jsleft)

    def getText(self,value):
        """定义获取文字的函数"""
        gtt = self.dr.find_element("xpath",value).text
        return gtt


    def tryTimesleep(self,value):
        """每一秒去寻找切换iframe框"""
        for i in range(10):
            try:
                self.dr.switch_to.frame(value)
            except:pass
            t.sleep(1)

    def trySendKeys(self,value,connect):
        """尝试去输入值"""
        for i in range(10):
            try:
                self.dr.find_element_by_xpath(value).send_keys(connect)
                break
            except:pass
            t.sleep(1)
        else:
            print("Find xpath filed")

    def tryText(self,value):
        """尝试获取文字的函数"""
        for i in range(10):
            try:
                 gt = self.dr.find_element("xpath",value).text
                 return gt
            except:pass
            t.sleep(1)

    def impLicitly(self,value):
        """显式等待"""
        self.dr.implicitly_wait(value)


    def switchOneWindows(self,value):
        """切换到浏览器窗口"""
        all_handers= self.dr.window_handles
        # print(all_handers)
        self.dr.switch_to_window(self.dr.window_handles[value])
        # print(self.dr.title)

    def getScreenShot(self,value):
        """截图"""
        self.dr.get_screenshot_as_file(value)

    def reFresh(self):
        """刷新页面"""
        self.dr.refresh()

    def dissMiss(self):
        """处理弹框"""
        self.dr.switch_to.alert().accept()
        # self.dr.switch_to.alert().dismiss()


    def Login(self,username,password):
        self.dr.get("http://10.248.26.37/ESOP/Login/login.do")
        t.sleep(1)
        self.dr.maximize_window()
        t.sleep(1)
        self.dr.find_element("xpath",".//*[@id='username']").clear()
        t.sleep(1)
        self.dr.find_element("xpath", ".//*[@id='username']").send_keys(username)
        t.sleep(2)
        self.dr.find_element("xpath",".//*[@id='password']").clear()
        t.sleep(1)
        self.dr.find_element("xpath",".//*[@id='password']").send_keys(password)
        t.sleep(2)
        self.dr.find_element("xpath","//*[contains(text(),'忘记密码')]/preceding-sibling::input[2]").click()

















































