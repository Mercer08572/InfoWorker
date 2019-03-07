#!D:\Python\python.exe
#-*- coding:utf-8 -*-
# datatime : 2019/3/4 16:52
# author : badbugu17
# file : DbTest
import os

import pymysql

# try:
#     # 获取数据库连接，设置编码为utf-8
#     conn = pymysql.connect(host='xxx.xxx.xxx.xxx', user='Collector', passwd='xxx', db='Social_Library',
#                            port=xxx, charset='utf8');
#     cur = conn.cursor(); # 获取一个游标
#     cur.execute('select * from Collection_User')
#     data = cur.fetchall()
#     for d in data:
#         print("ID:" + str(d[0]) + "用户名：" + str(d[1]));
#
#     cur.close();
#     conn.close();
#
# except Exception as e:
#     print(e)

connectInfo_path = os.path.abspath("..");
connectInfo_path = os.path.join(connectInfo_path,"resources\\connectionInfo.ini");

print(connectInfo_path);
