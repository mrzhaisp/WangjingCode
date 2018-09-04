#coding=utf-8
__author__ = 'zgd'
import sys,time
import unittest
from Commonlib.CreateReporter import CreateReporter
c = CreateReporter()
from Commonlib.send import SendEmail
s = SendEmail()
class Tsuit(unittest.TestCase):
    """制作用例集合"""
    def testT(self):
        #找到测试用例的文件路径
        case_dir = "../Test"
        #加载测试用例
        discover = unittest.defaultTestLoader.discover(case_dir,pattern="*.py",top_level_dir=None)
        # print(discover)
        #把测试执行的用例传给createReport,
        c.createReporter(discover)
        #调用邮箱类 把该路径下的测试报告通过邮箱发送
        s.sendEmail("../Reporter/37test.html")
        for i in range(100):
            k = i + 1
            str = '/' * i + '' * (100 - k)
            sys.stdout.write('\r' + str + '[%s%%]' % (i + 1))
            sys.stdout.flush()
            time.sleep(0.05)
        print(u"Emal send----->%100")
    #原因是因为sub_class里缺少runTest方法，不加上该方法，上边的tetsT会报错，直接在Tsuit的类中增加
    def runTest(self):
        pass

if __name__=='__main__':
    unittest.main()










