# -*- coding: UTF-8 -*-
import pymysql
from mysql_conn import config

class Mysql(object):
    __pool = None

    def __init__(self):
        self._conn = Mysql.__getConn()
        self._cursor = self._conn.cursor()

    @staticmethod
    def __getConn():
        """
        @summary: 静态方法 ，从连接池中取出连接
        @return MySQLdb.connection
        """
        if Mysql.__pool is None:
            __pool = pymysql.connect(host=config.DBHOST,
                                     port=config.DBPORT,
                                     user=config.DBUSER,
                                     passwd=config.DBPWD,
                                     db=config.DBNAME,
                                     charset=config.DBCHAR)
        return __pool

    def getOne(self, sql):
        try:
            self._cursor.execute(sql)
            data = self._cursor.fetchone()
            return data
        except Exception as ex:
            print(ex,ex)
        finally:
            self.close()

    def getAll(self, sql):
        try:
            self._cursor.execute(sql)
            data = self._cursor.fetchall()
            return data
        except Exception as ex:
            print(ex, ex)
        finally:
            self.close()

    def executeDML(self, sql):
        try:
            num = self._cursor.execute(sql)
            self._conn.commit()
            return num
        except Exception as ex:
            self._conn.rollback()
            print(ex, ex)
        finally:
            self.close()

    def close(self):
        if self._cursor:
            self._cursor.close()
        if self._conn:
            self._conn.close()
