# -*- coding: UTF-8 -*-
__author__ = 'fuhao'
# * Created by PyCharm.
# * User: fuhao
# * Date: 13-11-19
# * Time: 下午2:26
# * To change this template use File | Settings | File Templates.
from pymongo import Connection
import uploadFile2mongodb

filedir = r'D:\image'
con = Connection(host="10.23.4.208", port=27017)
db = con.imgdb
imgmongo = uploadFile2mongodb.mongoImg(db, filedir)
#imgmongo.insert()

#imgmongo.getbyname('D:\image\Fish.bmp',r'D:\Fish.bmp')
imgmongo.downloadFiles(r'D:/css/')
#imgmongo.deleteFiles()