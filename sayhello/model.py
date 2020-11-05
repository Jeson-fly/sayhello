#!/usr/bin/env python
# encoding: utf-8

'''
@author: lining
@file: model.py
@time: 2020/11/5 23:11
@desc: 模型
'''
from datetime import datetime

from sayhello import db


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(200))
    body = db.Column(db.String(200))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, index=True)  # index开启索引
