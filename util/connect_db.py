#!/usr/bin/env python3
# -*-coding:utf-8-*-
# __author__: hunter
import json

import pymysql.cursors

class OperationMysql:
    def __init__(self):
        self.conn = pymysql.connect(
            host = "localhost",
            prot = '3306',
            user = 'root',
            password = "123456",
            db = "HMW",
            charset = 'utf-8',
            cursorclass = pymysql.cursors.DictCursor
        )
        self.cur = self.conn.cursor()

    def search_one(self):
        self.cur.execute(pymysql)
        result = self.cur.fetchone()
        result = json.dumps(result)
        return result

if __name__ == "__main__":
    op_mysql = OperationMysql
    res = op_mysql.search_one("select * from web_user where Name='sdsa'")
    print(type(res))