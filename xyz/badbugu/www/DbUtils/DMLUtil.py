#!D:\Python\python.exe
#-*- coding:utf-8 -*-
# datatime : 2019/3/4 17:45
# author : badbugu17
# file : DMLUtil
from xyz.badbugu.www.DbUtils.ConnSingleton import ConnSingleton


class DMLUtil:



    def execMoreSql(self,sqlList):
        flag = 0; # 执行成功，标记为1  执行失败标记为0

        try:
            csl = ConnSingleton();
            cursor = csl.get_cursor();
            for sql in sqlList:
                cursor.execute(sql);
        except Exception as e :
            print(e);
        finally:
            ConnSingleton.close_cursor();


