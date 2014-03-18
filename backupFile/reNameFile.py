# -*- coding: UTF-8 -*-
__author__ = 'fuhao'

import os


def rename_files():
    path = 'C:\\Users\\fuhao\\Desktop\\temp'
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path,file))==True:
            newname = file.replace("tmp", "jpg")
            os.rename(os.path.join(path, file), os.path.join(path, newname))
            print(file)


if __name__ == '__main__':
    file_name= u'C:/Users/fuhao/Desktop/golang升级更新方法.txt'
    f = open(file_name, 'r')
    print f.read()