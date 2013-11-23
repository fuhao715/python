# -*- coding: UTF-8 -*-
__author__ = 'fuhao'
# * Created by PyCharm.
# * User: fuhao
# * Date: 13-11-21
# * Time: 下午4:34
# * To change this template use File | Settings | File Templates.
from pymongo import MongoClient
import datetime
from bson.objectid import ObjectId
from pymongo import ASCENDING, DESCENDING
client = MongoClient('10.23.4.208', 27017)
db = client.test
collection = db.person

post = {"author": "css123",
        "text": "My first blog post !",
        "tags": ["mongodb", "python", "pymongo"],
        "date": datetime.datetime.utcnow()}

posts = db.posts
post_id = posts.insert(post)
print post_id
print db.collection_names()
print posts.find_one()
print posts.find_one({"_id": post_id})
post_id_as_str = str(post_id)
print post_id_as_str
print posts.find_one({"_id": post_id_as_str})
print posts.find_one({"_id": ObjectId(post_id_as_str)})


def get(post_id):
    document = client.db.collection.find_one({'_id': ObjectId(post_id)})
    return document

new_posts = [{"author": "Mike",
               "text": "Another post!",
               "tags": ["bulk", "insert"],
               "date": datetime.datetime(2009, 11, 12, 11, 14)},
             {"author": "Eliot",
               "title": "MongoDB is fun",
               "text": "and pretty easy too!",
               "date": datetime.datetime(2009, 11, 10, 10, 45)}]
post_ids = posts.insert(new_posts)

for post in post_ids:
    print post

for post in posts.find():
    print post

for post in posts.find({"author": "Mike"}):
    print post

print posts.count()

print posts.find({"author": "Mike"}).count()

d = datetime.datetime(2009, 11, 12, 12)
for post in posts.find({"date": {"$lt": d}}).sort("author"):
    print post

print posts.find({"date": {"$lt": d}}).sort("author").explain()["cursor"]
print posts.find({"date": {"$lt": d}}).sort("author").explain()["nscanned"]

posts.create_index([("date", DESCENDING), ("author", ASCENDING)])
print posts.find({"date": {"$lt": d}}).sort("author").explain()["cursor"]
print posts.find({"date": {"$lt": d}}).sort("author").explain()["nscanned"]











