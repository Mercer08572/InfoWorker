#!D:\Python\python.exe
#-*- coding:utf-8 -*-
# datatime : 2019/3/4 17:45
# author : badbugu17
# file : DMLUtil
from xyz.badbugu.www.DbUtils.ConnSingleton import ConnSingleton


class DMLUtil:

    csl = ConnSingleton();

    '''
    批量处理如果出错，不应该回滚，应该忽略错误，并将错误SQL记录到错误表中
    '''
    def execMoreSql(self,sqlList):
        flag = 0; # 执行成功，标记为1  执行失败标记为0
        conn = None;

        tempSql = None;   # 存储当前操作的sql 如果发生异常，则将此变量中的sql写入 sqlLibrary/errorSqlList.sql 中
        errorSqlPath = os

        try:
            conn = self.csl.get_conn();
            cursor = conn.cursor();
            for sql in sqlList:
                tempSql = sql;
                cursor.execute(sql);
        except Exception as e :
            # conn.rollback();
            with open

            print(e);
        finally:
            # conn.commit();
            self.csl.close_conn();

        return;
