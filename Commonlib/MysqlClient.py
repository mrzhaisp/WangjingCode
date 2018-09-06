#coding=utf-8
__author__ = 'zgd'
from MySQLdb import *
import time
class MysqlClient():
    def __init__(self):
        # 创建数据库链接
        self.db=connect(host='127.0.0.1',
                          port=3306,
                          db='poorderinfo',
                          user='root',
                          passwd='mysql',
                          charset='utf8')
        #创建游标
        self.cs1 = self.db.cursor()

    def dateAdd(self,*args):
        """得到poordernumber存库"""
        try:
            #打开txt文件 读取txt文件内的单号  读取存库
            f = open("../DataShare/zykc-ordernumbs.txt").readlines()
            for line in f:
                list1 = line.replace('    ', ',')
                po = list1[0:16]
                tim = list1[17:36]
                ocd = list1[37:45]
            #游标去执行sql
            sql = """
            insert into poorders (poordernumber ,createdate,tag) VALUES ('%s','%s','%s')"""
            count = self.cs1.execute(sql %(po ,tim,ocd))
            print(count)
            self.db.commit()
        except Exception,e:
            print(e)
        finally:
            #关闭游标，关闭数据库连接
            self.cs1.close()
            self.db.close()

    def dateSelec(self):
        try:
            count = self.cs1.execute("SELECT a.poordernumber,a.createdate from poorders a ")
            result = self.cs1.fetchone()
            num = result[0]
            caeateTime = result[1]
            print(num)
            print(caeateTime)
            # print(result)
            self.db.commit()
        except Exception,e:
            print(e)
        finally:
            self.cs1.close()
            self.db.close()


# if __name__=='__main__':
    # f = open("../DataShare/zykc-ordernumbs.txt").readlines()
    # print(f)
    # for line in f:
        # print(line)
        # list1 = line.replace('    ',',')
        # print(list1)
        # po = list1[0:16]
        # print(po)
        # tim = list1[17:36]
        # print(tim)
        # ocd = list1[37:45]
        # print(ocd)
    # creaTeDate = tim
    # poorDerNumBer = po
    # tag = ocd
    # add = MysqlClient()
    # nuMs = [poorDerNumBer,creaTeDate,tag]
    # add.dateAdd(*nuMs)
    # M = MysqlClient()
    # M.dateSelec()

