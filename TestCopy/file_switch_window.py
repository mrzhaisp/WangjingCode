#coding=utf-8
__author__ = 'zhai'
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

import time as t
dr = webdriver.Firefox()
dr.get("http://10.248.26.37/ESOP/Login/login.do")
dr.maximize_window()
t.sleep(1)
dr.find_element("xpath",".//*[@id='username']").clear()
t.sleep(1)
dr.find_element("xpath", ".//*[@id='username']").send_keys("tdr")
t.sleep(2)
dr.find_element("xpath",".//*[@id='password']").clear()
t.sleep(1)
dr.find_element("xpath",".//*[@id='password']").send_keys("Cmcc@121122")
t.sleep(2)
dr.find_element("xpath","//*[contains(text(),'忘记密码')]/preceding-sibling::input[2]").click()
t.sleep(1)
for i in range(10):
    try:
        dr.switch_to.frame("iframe_ID_201")
        break
    except:pass
    t.sleep(1)
for i in range(10):
    try:
        dr.execute_script("arguments[0].scrollIntoView(); ", u".//span[text()='超时工单提醒']")
        break
    except:pass
    t.sleep(1)
dr.find_element("xpath",u".//*[@id='menuDiv']/descendant::div[text()='网络资源勘查']").click()
dr.switch_to.default_content()
for i in range(10):
    try:
        dr.switch_to.frame("iframe_ID_20321")
        break
    except:pass
    t.sleep(1)
for i in range(10):
    try:
        dr.find_element("xpath",".//*[@id='btnCustomerSelect-btnEl']").click()
        break
    except:pass
    t.sleep(1)

for i in range(10):
    try:
        dr.find_element_by_xpath(".//*[@id='keyWord']/descendant::input").send_keys(u"99回归")
        break
    except:pass
    t.sleep(1)
dr.find_element("xpath",u".//span[text()='查 询']/parent::button").click()
t.sleep(1)
dr.find_element("xpath", u".//div[contains(text(),'99回归87')]").click()
t.sleep(1)
dr.find_element("xpath",u".//span[text()='确定']/parent::button").click()
t.sleep(1)
dr.find_element("xpath",u".//*[contains(text(),'产品名称')]/following-sibling::div[1]/input").send_keys( u"数据专线2.0")
for i in range(10):
    try:
        dr.find_element("xpath",u".//li[contains(text(),'数据专线2.0')]").click()
        break
    except:pass
    t.sleep(1)
else:
    print(u"还没来得是输入值呢")
t.sleep(1)
dr.find_element("xpath",u".//*[contains(text(),'导入')]/parent::button").click()
t.sleep(2)
print(u"准备弹框了")
all_handers = dr.window_handles
print(all_handers)










