#coding=utf-8
__author__ = 'zgd'
from xml.dom import minidom
class Readxml():
    """定义读取xml文件"""
    def readxml(self):
        # root = minidom.parse("../DateShare/wangjing.xml")
        root = minidom.parse("D:\\WangjingCode\\DataShare\\wangjing.xml")
        #login这个组
        firstnode = root.getElementsByTagName("login")[0]
        print(firstnode)

        #找到login  组下的username节点里的值
        secondnode = firstnode.getElementsByTagName("username")[0].firstChild.data
        return secondnode
p = Readxml()
print(p.readxml())
# ,OneNode,TwoNode


















































































