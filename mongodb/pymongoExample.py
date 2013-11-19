# -*- coding: UTF-8 -*-
__author__ = 'fuhao'
# * Created by PyCharm.
# * User: fuhao
# * Date: 13-11-19
# * Time: 下午1:39
# * To change this template use File | Settings | File Templates.
import pymongo
client = pymongo.MongoClient("10.23.4.208", 27017)
db = client.test
print db.name
db.my_collection
db.my_collection.save({"x": 14})
db.my_collection.save({"x": 42})
db.my_collection.save({"x": 43})
print db.my_collection.find_one()
for item in db.my_collection.find():
    print item["x"]
db.my_collection.create_index("x")
for item in db.my_collection.find().sort("x", pymongo.ASCENDING):
    print item["x"]

print [item["x"] for item in db.my_collection.find().limit(2).skip(1)]