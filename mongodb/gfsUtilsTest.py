# -*- coding: UTF-8 -*-
__author__ = 'fuhao'
# * Created by PyCharm.
# * User: fuhao
# * Date: 13-11-19
# * Time: 下午5:12
# * To change this template use File | Settings | File Templates.
import gfsUtils
from bson.objectid import ObjectId

if __name__ == "__main__":
    gfs = gfsUtils.GFS.getInstance()
    if gfs:
        image_id = gfs.insert("D:/css123.jpg")
        print "==========Object id is %s  and it's type is %s==========" % (image_id , type(image_id))
        (data, dic) = gfs.get(ObjectId(image_id))
        # gfs.write_2_disk(data, dic)