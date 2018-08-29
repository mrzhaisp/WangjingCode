#coding=utf-8
__author__ = 'zgd'
from xml.dom import minidom
class Readxml():
    """定义读取xml文件"""
    def readxml(self,oneNode,twoNode):
    # def readxml(self):
    #     root = minidom.parse("../DateShare/wangjing.xml")
    #     root = minidom.parse("E:\\WangjingCode\\DataShare\\wangjing.xml")
        root = minidom.parse("D:\\WangjingCode\\DataShare\\wangjing.xml")
        #login这个组
        # firstnode = root.getElementsByTagName("poorder")[0]
        firstnode = root.getElementsByTagName(oneNode)[0]


        #找到login  组下的username节点里的值
        # secondnode = firstnode.getElementsByTagName("epxect")[0].firstChild.data
        secondnode = firstnode.getElementsByTagName(twoNode)[0].firstChild.data
        # print(secondnode)
        return secondnode
#
# p = Readxml()
# print(p.readxml())
# ,OneNode,TwoNode


















































































