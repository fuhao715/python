# -*- coding: UTF-8 -*-
__author__ = 'fuhao'
# * Created by PyCharm.
# * User: fuhao
# * Date: 13-10-24
# * Time: 下午3:23
# * To change this template use File | Settings | File Templates.
import os
import re
current_path = os.getcwd()
#print current_path + '\n'


def wald_dir(dir, fileinfor, topdown=True):
    for root, dirs, files in os.walk(dir, topdown):
        for name in files:
            #print os.path.join(root, name)
            find_information(os.path.join(root, name), fileinfor)
        for name in dirs:
            print os.path.join(root, name)


def find_information(log_file, infor):
    txt = open(log_file, 'r')
    context = txt.read()
    if re.search(infor, context):
        print '%s ' % (log_file[log_file.find('domains/')+8:])
        txt.seek(0)
        count = 0
        for (line, value) in enumerate(txt):
            index = value.find(infor)
            if index != -1:
                count += 1
                if count == 10:
                    raw_input("请输入Enter继续查看:\n")
                    count = 0
                print '%d  %s \n' % (line, value)
    txt.close()


print current_path + '/logs'
infor = raw_input('请输入要查找的字符串:\n')
wald_dir(current_path + '/logs', infor)

