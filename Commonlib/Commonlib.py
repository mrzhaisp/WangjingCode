#coding=utf-8
# __author__ = 'zgd'
import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time as t
class Commonlib():
    def __init__(self):
        """加载firefox配置文件"""
        # self.dr = webdriver.Firefox(webdriver.FirefoxProfile("C:\Users\Administrator\AppData\Roaming\Mozilla\Firefox\Profiles\glw65f77.default"))
        self.dr = webdriver.Firefox()

    def openBrowser(self,myurl):
        """打开浏览器"""
        self.dr.get(myurl)
        self.dr.maximize_window()

    def closeBrowser(self):
        """关闭当前聚焦点所在的浏览器"""
        self.dr.close()

    def quitBrowser(self):
        """关闭所有窗口，安全关闭session"""
        self.dr.quit()

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
        jsleft = 'document.getElementsByClassName("x-scroller-ct")[0].scrollLeft=900'
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
        print(all_handers)
        self.dr.switch_to_window(self.dr.window_handles[value])
        # print(self.dr.title)

    def getScreenShot(self,value):
        """截图"""
        self.dr.get_screenshot_as_file(value)

    def reFresh(self):
        """刷新页面"""
        self.dr.refresh()

    def dissMissAlter(self):
        """处理弹框"""
        alsk = self.dr.switch_to_alert()
        alsk.accept()
        # self.dr.switch_to.alert().dismiss()

    def promptAlter(self):
        Alterprompt = self.dr.switchTo().alter

    def Login(self,username,password):
        """登录公共流程"""
        self.dr.get("http://10.248.50.222:7301/ESOP/Login/login.do")
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

    def PoorderShen(self,username,password):
        """审批时公共流程"""
        self.Login(username, password)
        self.waite(2)
        self.tryTimesleep("iframe_ID_201")
        self.tryMoveLocation(u".//span[text()='超时工单提醒']")
        self.waite(2)
        self.activeEvent(u".//*[@id='menuDiv']/descendant::div[text()='业务开通']")
        self.waite(2)
        self.shiFangFrame()
        self.waite(2)
        self.tryFindIframe("iframe_ID_2043")
        self.activeEvent(".//*[@id='btnCustomerSelect-btnEl']")
        self.waite(2)
        self.inputKeys(u".//*[@id='keyWord-bodyEl']/input", u"99回")
        self.waite(1)
        self.activeEvent(u".//span[text()='查 询']/parent::button")
        self.waite(1)
        self.activeEvent(u".//*[contains(text(),'99回归87')]")
        self.waite(1)
        self.activeEvent(u".//*[contains(text(),'确定')]/parent::button")
        self.waite(2)
        self.inputKeys(".//*[@id='poSpecName']/descendant::input", u"数据专线2.0")
        self.waite(2)
        self.activeEvent(".//*[@id='btnProductSpecSelect-btnEl']")
        self.waite(2)
        self.activeEvent(".//*[@id='window_vipLinePre-body']/following-sibling::div[1]/descendant::button[1]")
        self.waite(2)
        # 找到合同点击合同
        self.activeEvent(".//*[@id='poAgreementId-triggerWrap']/div")
        self.waite(2)
        self.activeEvent(u".//*[contains(text(),'开通的合同')]")
        self.waite(2)
        # 期望保证等级
        self.activeEvent(".//*[@id='vipGrid-body']/descendant::td[10]")
        self.waite(2)
        self.activeEvent(".//*[@id='vipGrid-body']/div[2]/div[1]/div[1]/div[2]/div[1]")
        self.waite(1)
        # 选择A级服务
        self.activeEvent(u".//*[contains(text(),'普通级')]")
        # 安装调测费用
        self.activeEvent(".//*[@id='vipGrid-body']/descendant::td[13]")
        self.waite(3)
        self.inputKeys(".//*[@id='vipGrid-body']/div[2]/descendant::input", "500")
        self.waite(2)
        # A段结算比例
        self.activeEvent(".//*[@id='vipGrid-body']/descendant::td[14]")
        self.waite(2)
        self.inputKeys(".//*[@id='vipGrid-body']/div[3]/descendant::input", "50")
        # Z端结算比例
        self.activeEvent(".//*[@id='vipGrid-body']/descendant::td[15]")
        self.waite(2)
        self.inputKeys(".//*[@id='vipGrid-body']/div[4]/descendant::input", "50")
        # 功能费套餐选项
        self.activeEvent(".//*[@id='vipGrid-body']/descendant::td[16]/descendant::input")
        self.waite(2)
        self.activeEvent(".//*[@id='poPolicyForm_vipLine-body']/descendant::input[1]")
        self.waite(2)
        self.inputKeys(".//*[@id='poPolicyForm_vipLine-body']/descendant::input[2]", "666")
        self.waite(2)
        self.activeEvent(u".//*[text()='清空']/ancestor::div[1]/preceding-sibling::div/descendant::button")
        self.waite(2)
        self.tryMoveLocation(u".//*[contains(text(),'账期生效规则')]")
        self.waite(1)
        self.jsLeft()
        # 功能费A段结算比例
        self.waite(2)
        self.activeEvent(".//*[@id='vipGrid-body']/descendant::td[18]")
        self.waite(2)
        self.inputKeys(".//*[@id='vipGrid-body']/div[5]/descendant::input", "50")
        self.waite(2)
        # 功能费Z段结算比例
        self.activeEvent(".//*[@id='vipGrid-body']/descendant::td[19]")
        self.waite(2)
        self.inputKeys(".//*[@id='vipGrid-body']/div[6]/descendant::input", "50")
        self.waite(2)
        # 支付模式
        self.activeEvent(".//*[@id='businessModeCombo-triggerWrap']/div[1]")
        self.waite(1)
        self.activeEvent(u".//*[text()='一点支付']")
        self.waite(1)
        # 账期生效规则
        self.activeEvent(".//*[@id='effectRuleCombo-triggerWrap']/div[1]")
        self.waite(1)
        self.activeEvent(u".//*[contains(text(),'下账期生效')]")
        # 签约主体
        self.waite(1)
        self.activeEvent(".//*[@id='contractMainId-triggerWrap']/div[1]")
        self.waite(1)
        self.activeEvent(u".//li[contains(text(),'有限分公司')]")
        self.waite(1)
        self.activeEvent(".//*[@id='submitButton-btnEl']")
        self.waite(2)
        self.activeEvent(".//*[text()='Yes']/parent::button")
        self.waite(2)
        self.activeEvent(".//*[@id='poFirstNode-triggerWrap']/div")
        self.waite(2)
        self.activeEvent(u".//*[@id='window_poRateplan_vipline']/following-sibling::div[12]/descendant::li")
        self.waite(2)
        self.activeEvent(".//*[@id='window_poRateplan_vipline']/following-sibling::div[9]/descendant::button[1]")











































