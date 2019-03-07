#!D:\Python\python.exe
#-*- coding:utf-8 -*-
# datatime : 2019/3/5 11:07
# author : badbugu17
# file : Sun

class Sun:
    __temp = "Hello";

    def __init__(self):
        print("1234");
        return

    def Hi(self):
        print("HI");
        return

    @staticmethod
    def NiHao():
        print("你好");
        return


if __name__ == "__main__":
    sun = Sun();
    sun.Hi();

    Sun.NiHao();