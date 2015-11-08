
# -*- coding: utf-8 -*-

import pymssql

from my_log import log_set



DB_CHARSET = 'utf8'
DB_HOST ='127.0.0.1'
DB_USER='root'
DB_PWD ='fuhan'
DB_PORT = '3306'
DB_NAME ='xx'

import pymssql


class MSSQL:
    """
    对pymssql的简单封装
    pymssql库，该库到这里下载：http://www.lfd.uci.edu/~gohlke/pythonlibs/#pymssql
    使用该库时，需要在Sql Server Configuration Manager里面将TCP/IP协议开启

    用法：

    """

    def __init__(self,host,user,pwd,db):
        self.host = host
        self.user = user
        self.pwd = pwd
        self.db = db

    def __GetConnect(self):
        """
        得到连接信息
        返回: conn.cursor()
        """
        if not self.db:
            raise(NameError,"没有设置数据库信息")
        self.conn = pymssql.connect(host=self.host,user=self.user,password=self.pwd,database=self.db,charset="utf8")
        cur = self.conn.cursor()
        if not cur:
            raise(NameError,"连接数据库失败")
        else:
            return cur

    def ExecQuery(self,sql):
        cur = self.__GetConnect()
        cur.execute(sql)
        resList = cur.fetchall()

        #查询完毕后必须关闭连接
        self.conn.close()
        return resList

    def ExecNonQuery(self,sql):
        """
        执行非查询语句

        调用示例：
            cur = self.__GetConnect()
            cur.execute(sql)
            self.conn.commit()
            self.conn.close()
        """
        cur = self.__GetConnect()
        cur.execute(sql)
        self.conn.commit()
        self.conn.close()

ms = MSSQL(host="localhost",user="root",pwd="fuhan",db="xx")

def save_info(flight,id):
    resList = ms.ExecQuery("INSERT INTO flight( flight,del_id) VALUES (%s,%s);"%(flight,str(id)))
    print(resList)
    return resList

def get_info_list():
    resList = ms.ExecNonQuery("SELECT * FROM flight;")
    return resList
def get_info(flight):
    resList = ms.ExecNonQuery("SELECT * FROM flight WHERE flight =%s;" % flight)
    return resList

def del_info(flight):
    resList = ms.ExecNonQuery("DELETE * FROM flight WHERE flight =%s;" % flight)
    return resList
save_info(44, '7890')
print(get_info(44))