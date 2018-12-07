#！/usr/bin/env python
# -*- ccoding:UTF-8 -*-
import pymysql
abc=pymysql.connect(host='192.168.0.1',
                    port=3306,
                    user='root',
                    password='123123',
                    charset='utf8')
aaa=abc.cursor()
aaa.execute('usr 1;')
aaa.execute('select * from 1;')
print(aaa.fetchall())
print(aaa.fetchmany())
print(aaa.fetchall())
print(aaa.fetchone())
