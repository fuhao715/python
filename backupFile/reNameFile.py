# -*- coding: UTF-8 -*-
__author__ = 'fuhao'

import os
import re

def rename_files():
    # path = 'C:\\Users\\fuhao\\Desktop\\temp'
    path = u'E:/电影/'
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path,file))==True:
            strinfo = re.compile(u'^\[.*?\]') # [电影天堂www.dy2018.com]速度与激情6加长版BD中英双字
            if re.match(strinfo, file):
                print file
                newname = strinfo.sub('', file)
                # newname = file.replace("tmp", "jpg")
                os.rename(os.path.join(path, file), os.path.join(path, newname))
                print(file)



if __name__ == '__main__':
    #file_name= u'C:/Users/fuhao/Desktop/golang升级更新方法.txt'
    #f = open(file_name, 'r')
    #print f.read()
    rename_files()