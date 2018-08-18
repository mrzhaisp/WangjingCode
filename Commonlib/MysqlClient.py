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
            # count = cs1.execute("insert into poorders (poordernumber,createdate) VALUES ("+poorDerNumBer+","+creaTeDate+")")
            value = [poorDerNumBer,creaTeDate]
            count = cs1.execute("insert into poorders (poordernumber ,createdate) VALUES (%s ,%s)",value)
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
#     creaTeDate = time.strftime("%Y-%m-%d %H:%M:%S") + '--ocdzykc'
#     poorDerNumBer = "000808804832432"
#     add = MysqlClient()
#     nuMs = [poorDerNumBer,creaTeDate]
#     add.dateAdd(*nuMs)



        # se = MysqlClient()
    # se.dateSelec()