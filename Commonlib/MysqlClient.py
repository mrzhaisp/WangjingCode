#coding=utf-8
__author__ = 'zgd'
from MySQLdb import *
import time
class MysqlClient():
    def dateAdd(self,*args):
        try:
            #创建数据库连接
            conn = connect(host='127.0.0.1', port=3306, db='poorderinfo', user='root', passwd='mysql', charset='utf8')
            #创建游标
            cs1 = conn.cursor()
            #读取存入txt的单号和tag和创建时间
            f = open("../DataShare/zykc-ordernumbs.txt").readlines()
            for line in f:
                list1 = line.replace('    ', ',')
                po = list1[0:16]
                tim = list1[17:36]
                ocd = list1[37:45]
            # count = cs1.execute("insert into poorders (poordernumber,createdate) VALUES ("+poorDerNumBer+","+creaTeDate+")")
            #     value = [poorDerNumBer,creaTeDate,tag]
            # count = cs1.execute("insert into poorders (poordernumber ,createdate,tag) VALUES (%s ,%s,%s)",value)
            sql = """
            insert into poorders (poordernumber ,createdate,tag) VALUES ('%s','%s','%s')"""
            count = cs1.execute(sql %(po ,tim,ocd))
            print(count)
            conn.commit()
        except Exception,e:
            print(e)
        finally:
            cs1.close()
            conn.close()

    def dateSelec(self):
        try:
            #创建数据库连接
            conn = connect(host='127.0.0.1', port=3306, db='poorderinfo', user='root', passwd='mysql', charset='utf8')
            #创建游标
            cs1 = conn.cursor()
            count = cs1.execute("SELECT a.poordernumber,a.createdate from poorders a ")
            result = cs1.fetchone()
            num = result[0]
            caeateTime = result[1]
            print(num)
            print(caeateTime)
            # print(result)
            conn.commit()
        except Exception,e:
            print(e)
        finally:
            cs1.close()
            conn.close()


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


