#coding=utf-8
__author__ = 'zgd'
import sys
sys.getdefaultencoding() != 'utf-8'
reload(sys)
sys.setdefaultencoding('utf-8')

import HTMLTestRunner
class CreateReporter():
    """制作测试报告，把测试执行的结果传进来，discover方法执行的用例结果传进来"""
    #找到加载完全的用例
    def createReporter(self,mysuit):
        #定义测试报告的路径文件夹
        filepath='../Reporter/37test.html'
        with open(filepath,'wb') as ftm:
            HTMLTestRunner.HTMLTestRunner(
                stream=ftm,
                verbosity=2,
                title=u'37环境报告',
                description=u'37数据专线2.0测试报告'
            ).run(mysuit)















