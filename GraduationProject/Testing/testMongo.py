#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import re

import MySQLdb
import nltk
import arabicstemmer

import json
import os
import requests
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.stem.isri import ISRIStemmer
import facebook
import pymongo

from pymongo import MongoClient
# client=MongoClient
# client=MongoClient('localhost',27018)
# print(client)
# client=MongoClient('mongodb://localhost:27018/')
# db=client.test_database
#
# collection=db.test_collection
# print("islam Amer1")
# post={
#     "id":"1",
#     "name":"islam",
# }
# print("islam Amer2")
#
# posts=db.posts
# post_id=posts.insert_one(post).inserted_id
# print(post_id)
# print("islam Amer3")
db = MySQLdb.connect("127.0.0.1", "root", "", "DATA", charset='utf8')
cur = db.cursor()

cur.execute("""SELECT * FROM test""" )
posts=cur.fetchall()

for i in posts:
    print(i[1])