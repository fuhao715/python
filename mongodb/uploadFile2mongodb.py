# -*- coding: UTF-8 -*-
__author__ = 'fuhao'
# * Created by PyCharm.
# * User: fuhao
# * Date: 13-11-19
# * Time: 下午2:23
# * To change this template use File | Settings | File Templates.
__metaclass__ = type

import os
from pymongo.database import Database
import time
import gridfs


class mongoImg(object):
    """mongoInsert is a class for inserting document


    """
    def __init__(self, database, dir):
        """Create a new instance of :class:mongoInsert
        :Parameters:
          - `database`: database to use
          - `dir` : directory of document
          """
        if not isinstance(database, Database):
            raise TypeError("database must be an instance of Database")
        if len(dir) < 1:
            raise TypeError("dir must be an string of directory")

#         self.__con = Connection()
        self.__imgdb = database
        self.__imgfs = gridfs.GridFS(self.__imgdb)
        self.__dir = dir
        self.__filelist = []

    #save filepath in list.txt
    def __dirwalk(self, topdown=True):
        """traverse the documents of self.__dir and save in self.__filelist
        """
        sum=0

        # self.__filelist.clear()
        del self.__filelist[:]

        for root, dirs, files in os.walk(self.__dir, topdown):
            for name in files:
                sum += 1
                temp = os.path.join(root, name)
                print temp
                self.__filelist.append(temp)
        print(sum)

    #insert image
    def insert(self):
        """insert images in mongodb
        """
        self.__dirwalk()

        tStart = time.time()
        for fi in self.__filelist:
            print 'fi=%s ' % fi[fi.rfind('\\')+1:]
            with open(fi, 'rb') as myimage:
                data = myimage.read()
                self.__imgfs.put(data, content_type="bmp", filename=fi[fi.rfind('\\')+1:])

        tEnd = time.time()
        print ("It cost %f sec" % (tEnd - tStart))

    #get image by filename
    def downloadbyname(self, filename, savepath):
        """get img from mongdb by filename
        """
        if len(savepath) < 1:
            raise TypeError("dir must be an string of directory")

        dataout = self.__imgfs.get_version(filename)
        # try:
        imgout = open(savepath+filename, 'wb')
        data = dataout.read()
        imgout.write(data)
        # finally:
        imgout.close()

    def downloadFiles(self, localPath):
        if len(localPath) < 1:
            raise TypeError("dir must be an string of directory")

        fileList = self.__imgfs.list()

        for filename in fileList:
            dataout = self.__imgfs.get_version(filename)
            imgout = open(localPath+filename, 'wb')
            data = dataout.read()
            imgout.write(data)
            imgout.close()

    def deleteFile(self, filename):
        pass

    def deleteFiles(self):
        pass

    def findbyname(self, filename):
        pass

    def findAll(self):
        pass