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
self.activeEvent(".//*[@id='vipGrid-body']/div[4]/div[1]/descendant::div[4]")
self.waite(1)
# 选择A级服务
self.activeEvent(".//*[@id='window_vipLinePre']/following-sibling::div[20]/descendant::li[3]")
# 安装调测费用
self.activeEvent(".//*[@id='vipGrid-body']/descendant::td[13]")
self.waite(2)
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
