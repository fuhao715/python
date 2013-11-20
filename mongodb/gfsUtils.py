# -*- coding: UTF-8 -*-
__author__ = 'fuhao'
# * Created by PyCharm.
# * User: fuhao
# * Date: 13-11-19
# * Time: 下午5:06
# * To change this template use File | Settings | File Templates.
from pymongo import Connection
from gridfs import *
import threading,time
from bson.objectid import ObjectId
#文件处理系统
class GFS:
    #定义connection and fs
    conn = None
    db = None
    fs = None
    instance = None
    locker = threading.Lock()

    #初始化
    def __init__(self):
        print "__init__"
        GFS._connect()
        print "server info " + " * " * 40
        print GFS.conn.server_info

    #获得单列对象
    @staticmethod
    def getInstance():
        GFS.locker.acquire()
        try:
            GFS.instance
            if not GFS.instance:
                GFS.instance = GFS()
            return GFS.instance
        finally:
            GFS.locker.release()

    #写入,返回文件id号
    def insert(self, name):
        my_file = None
        try:
            my_file = open(name, 'rb')
            data = my_file.read()
            print "name is %s" % name
            with GFS.fs.new_file() as fp:
                fp.write(data)
                fp.close()
                return fp._id
        finally:
            try:
                my_file.close()
            finally:
                GFS.conn = None
                GFS._connect()

    def update(self, file_id):
        pass

    def getByFileID(self, file_id):
        return list(GFS.db.fs.chunks.find(dict(files_id=file_id)))

    #获得图片
    def getByName(self, name):
        gf = None
        try:
            gf = GFS.fs.open(name, "r")
            print gf
            im = gf.read()
            dic = {}
            dic["chunk_size"] = gf.chunk_size
            dic["metadata"] = gf.metadata
            dic["mode"] = gf.mode
            dic["length"] = gf.length
            dic["upload_date"] = gf.upload_date
            dic["name"] = gf.name
            dic["content_type"] = gf.content_type
            return (im,dic)
        except Exception, e:
            print e
            return (None, None)
        finally:
                if gf:
                    if not gf.closed:
                        gf.close()


    #获得文件列表
    def list(self):
        return list(self.db.fs.files.find())

    #删除文件,name is fileID
    def remove(self, name):
        GFS.fs.delete(name)

    @staticmethod
    def _connect():
        if not GFS.c:
            GFS.conn = Connection("10.23.4.208", 27017)
            GFS.db = GFS.conn.imgdb
            GFS.fs = GridFS(GFS.db)


if __name__ == "__main__":
    gfs = GFS.getInstance()
    if gfs:
        image_id = gfs.put("D:/css.jpg")
        print "==========Object id is %s  and it's type is %s==========" % (image_id , type(image_id))
        (data, dic) = gfs.get(ObjectId(image_id))
        gfs.write_2_disk(data, dic)