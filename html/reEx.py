# -*- coding: UTF-8 -*-
__author__ = 'fuhao'
# * Created by PyCharm.
# * User: fuhao
# * Date: 14-3-19
# * Time: 上午10:32
# * To change this template use File | Settings | File Templates.
import re
# name = u'【6v电影www.dy131.com】逃出克隆岛BD中英双字1024高清CD4.rmvb'
name = u'[电影天堂www.dy2018.com]速度与激情6加长版BD中英双字'
strinfo = re.compile(u'^\[.*\]')
if re.match(strinfo, name):
    name = strinfo.sub('', name)
    print name

print name

a = u'中国'
b = u'.中国'
print type(a)
if a in b:
    print a

import os
path = u'E:/电影/'
for file in os.listdir(path):
        if os.path.isfile(os.path.join(path,file))==True:
            print type(os.path.join(path,file)),os.path.join(path,file)