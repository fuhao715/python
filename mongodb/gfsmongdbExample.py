# -*- coding: UTF-8 -*-
__author__ = 'fuhao'
# * Created by PyCharm.
# * User: fuhao
# * Date: 13-11-20
# * Time: 上午11:24
# * To change this template use File | Settings | File Templates.
import pymongo
import gridfs
from bson.objectid import ObjectId
conn = pymongo.Connection("10.23.4.208", 27017)
db = conn.imgdb
fs = gridfs.GridFS(db)
#print list(db.fs.files.find())

with fs.get(ObjectId('528c1b17e209d4034c58684b')) as fp_read:
    print '----------\n'+fp_read.read()+'\n----------'


fa = fs.put('This is my new file1. It is teh awezum!')


print list(db.fs.files.find())
print '\n---------------\n'
#print list(db.fs.chunks.find())


fb = fs.put('This is file number 1. It should be split into several chunks')


print '----------\n'+str(fa)+'\n----------'
print '----------\n'+str(fb)+'\n----------'
print list(db.fs.chunks.find(dict(files_id=fa)))

with fs.get(fb) as fp_read:
    print '----------\n'+fp_read.read()+'\n----------'


fc = fs.put(fs.get(fa),filename='foo',bar='baz')
out = fs.get(fc)
print out.read()
print out.filename
print out.bar
print out.upload_date



with fs.new_file() as fp:
    fp.write('css in china')
    fp.close
print fp
print fp._id

with fs.get(fp._id) as fp_r:
    print fp_r.read()

with fs.new_file(chunkSize=10) as fp_size:
    fp_size.write('css chunckSize is 10,css hxzg_xt')
    fp_size.close()

with fs.get(fp_size._id) as fp_size_r:
    print fp_size_r.read()

print '\n---------------\n'
print list(db.fs.files.find())
print '\n---------------\n'
print list(db.fs.chunks.find(dict(files_id=fp_size._id)))
for ch in db.fs.chunks.find():
    #print ch
    pass