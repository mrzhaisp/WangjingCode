#coding=utf-8
__author__ = 'zgd'
from MySQLdb import *
class MysqlClient():
    def dateAdd(self):
        try:
            #创建数据库连接
            conn = connect(host='127.0.0.1', port=3306, db='poorderinfo', user='root', passwd='mysql', charset='utf8')
            #创建游标
            cs1 = conn.cursor()
            count = cs1.execute("insert into poorders (poordernumber,createdate) VALUES ('000808804832432','20180815232')")
            print(count)
            conn.commit()
        except Exception,e:
            print(e)
        finally:
            cs1.close()
            conn.close()
if __name__=='__main__':
    add = MysqlClient()
    add.dateAdd()
