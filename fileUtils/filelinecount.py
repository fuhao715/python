# -*- coding: UTF-8 -*-
__author__ = 'fuhao'
# * Created by PyCharm.
# * User: fuhao
# * Date: 13-11-15
# * Time: 下午3:47
# * To change this template use File | Settings | File Templates.
import sys
import os

exts = ['.html', '.js', '.css', '.java', '.py', '.xml', '.h', '.c', 'cpp', '.properties']
def read_line_count(fname):
    count = 0
    for file_line in open(fname).xreadlines():
        count += 1
    return count

if __name__ == '__main__':

    count = 0
    fcount = 0
    for root, dirs, files in os.walk(os.getcwd()):
        for f in files:
            # Check the sub directorys
            fname = (root + '/'+f)
            ext = os.path.splitext(fname)[1]  #f[f.rindex('.'):]
            try:
                if(exts.index(ext) >= 0):
                    fcount += 1
                    c = read_line_count(fname)
                    count += c
            except:
                pass

    print 'file count:%d' % fcount
    print 'count:%d' % count