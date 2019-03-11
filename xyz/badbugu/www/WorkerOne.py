#!D:\Python\python.exe
#-*- coding:utf-8 -*-
# datatime : 2019/3/1 15:26
# author : badbugu17
# file : WorkerOne
import os


def readCsv():

    # abspath = os.path.abspath('../../../');
    # abspath = abspath + "\\CsvLibrary\\生活家用户信息.csv"
    # userInfo = open('../../../CsvLibrary/生活家用户信息.csv',mode='r',encoding='UTF-8');
    # first_line = userInfo.readline();
    # print(first_line);
    # print('\n');
    # userInfo.close();

    abspath = os.path.abspath('');
    # abspath = os.path.join(abspath,"\\CsvLibrary\\生活家用户信息.csv");
    csvPath = os.path.join(abspath,"CsvLibrary/生活家用户信息.csv");  # csv文件存储的位置
    sqlFolderPath = os.path.join(abspath, "sqlLibrary");
    print(abspath);
    print(csvPath);
    print(sqlFolderPath);

    with open(csvPath,mode='r',encoding='UTF-8') as csv:
        line = csv.readline();
        line = line[:-2];        # 去除每一行末尾的换行符

        countLine = 0;
        while line:
            print(line);
            line = csv.readline();
            line = line[:-2];  # 去除每一行末尾的换行符

            if countLine == 0:   # 第一条为表头，不进行数据处理
                countLine += 1;
                continue;

            list = line.split(',');
            sqlTemplate = "INSERT INTO Collection_User (user_id," \
                          "user_name," \
                          "sex," \
                          "user_phone," \
                          "user_email," \
                          "card_no," \
                          "address1," \
                          "address2," \
                          "account_name," \
                          "bank_account," \
                          "lhhcode," \
                          "c_account_addr," \
                          "user_bankadd," \
                          "recBranchName," \
                          "recBranchProvince," \
                          "recBranchCity," \
                          "c_manager_name," \
                          "source," \
                          "insert_date," \
                          "insert_year," \
                          "insert_month)" \
                          "VALUES('{user_id}'," \
                          "'{user_name}'," \
                          "'{sex}'," \
                          "'{user_phone}'," \
                          "'{user_email}'," \
                          "'{card_no}'," \
                          "'{address1}'," \
                          "'{address2}'," \
                          "'{account_name}'," \
                          "'{bank_account}'," \
                          "'{lhhcode}'," \
                          "'{c_account_addr}'," \
                          "'{user_bankadd}'," \
                          "'{recBranchName}'," \
                          "'{recBranchProvince}'," \
                          "'{recBranchCity}'," \
                          "'{c_manager_name}'," \
                          "'{source}'," \
                          "'{insert_date}'," \
                          "'{insert_year}'," \
                          "'{insert_month}')".format(user_id=__strFormat(list[0]),user_name=__strFormat(list[1]),sex=__strFormat(list[2]),user_phone=__strFormat(list[3]),user_email=__strFormat(list[4]),card_no=__strFormat(list[5]),address1=__strFormat(list[6]),address2=__strFormat(list[7]),account_name=__strFormat(list[8]),bank_account=__strFormat(list[9]),lhhcode=__strFormat(list[10]),c_account_addr=__strFormat(list[11]),user_bankadd=__strFormat(list[12]),recBranchName=__strFormat(list[13]),recBranchProvince=__strFormat(list[14]),recBranchCity=__strFormat(list[15]),c_manager_name=__strFormat(list[16]),source='',insert_date='',insert_year='',insert_month='') ;
            # print(list)
            # print(sqlTemplate);

            if countLine == 15:  # 第一次，先处理15条记录
                break;

            countLine += 1;

    print('本次处理数据 %d 条。' %(countLine));

    return;

# 将导出文件中的双引号去除
def __strFormat(str):
    str = str[1:-1];
    return str;



if __name__ == '__main__':
    readCsv();
