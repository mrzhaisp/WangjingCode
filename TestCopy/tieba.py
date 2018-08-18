#!/usr/bin/env python
# -*- coding:utf-8 -*-

#import requests
import urllib2
import urllib
# 导入lxml库的 etree类，用来将html文件转换为 HTML DOM，方便使用xpath提取
from lxml import etree

class Tieba:
    def __init__(self):
        self.tiebaName = raw_input("请输入需要爬取的贴吧:")
        self.beginPage = int(raw_input("请输入爬取的起始页："))
        self.endPage = int(raw_input("请输入爬取的结束页："))
        self.baseURL = "http://tieba.baidu.com"
        #self.headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.86 Safari/537.36"}
        self.headers = {"User-Agent" : "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1 Trident/5.0;"}

    def startWork(self):
        """
            发送贴吧每一页的url请求
        """
        for page in range(self.beginPage, self.endPage + 1):
            pn = (page - 1) * 50
            keyword = {"kw" : self.tiebaName, "pn" : pn}
            kw = urllib.urlencode(keyword)
            url = self.baseURL + "/f?" + kw
            #print url
            html = self.loadRequest(url)
            self.loadPage(html)

    def loadRequest(self, url):
        """
            发送请求，返回响应
            url: 发送请求的url地址
        """
        request = urllib2.Request(url, headers = self.headers)
        #request = urllib2.Request(url)
        response = urllib2.urlopen(request)
        return response.read()

    def loadPage(self, html):
        """
            提取每个帖子的url，并发送请求，获取响应
            html: 贴吧每一页的html

        """
        content = etree.HTML(html)
        #print content
        # xpath 返回的所有匹配成功后的结果的列表
        #pagelink_list = content.xpath("//div[@class='threadlist_lz clearfix']/div/a[@class='j_th_tit']/@href")
        pagelink_list = content.xpath("//div[@class='col2_right j_threadlist_li_right']//div/a/@href")
        pagelink_list = content.xpath("//div[@class='t_con cleafix']//div/a/@href")
        for link in pagelink_list:
            print link
            self.loadImage(self.loadRequest(self.baseURL + link))

    def loadImage(self, html):
        """
            提取帖子里用户发送的图片的url地址
            html: 每个帖子的html

        """
        content = etree.HTML(html)
        imagelink_list = content.xpath("//div[@class='p_content  ']//img[@class='BDE_Image']/@src")
        for link in imagelink_list:
            self.writeImage(self.loadRequest(link), link[-10:])

    def writeImage(self, data, filename):
        """
            将图片的响应数据，写入到本地磁盘里
            data: 图片的响应数据
            filename: 文件名(图片url的后10位)
        """
        print "正在保存图片...%s" % filename
        with open(filename, "wb") as f:
            f.write(data)

if __name__ == "__main__":
    tieba = Tieba()
    tieba.startWork()



