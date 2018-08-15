#coding=utf-8
__author__ = 'zgd'
# import MySQLdb

import pymysql
class MysqlClient():
    def insertDate(self):
        try:
            #创建数据库连接
            conn = connect(
                host = 'localhost',
                port = 3306,
                db = 'poorder',
                user='root',
                passwd='mysql',
                charset='utf8')
            #创建游标
            cs1 = conn.cursor()
            sql = 'INSERT INTO poorder VALUES (%s,%s,%s)'
            dates = [
                (1,'1898912121','2017-01-08')
                ]
            cs1.execute(sql,dates)
            cs1.commit()
        except Exception,e:
            print(e)
        finally:
            cs1.close()
            conn.close()

if __name__=='__main__':

    M2 = MysqlClient()
    M2.insertDate()




















