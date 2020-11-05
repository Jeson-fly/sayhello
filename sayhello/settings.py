#!/usr/bin/env python
# encoding: utf-8

'''
@author: lining
@file: settings.py
@time: 2020/11/5 22:38
@desc: 配置文件
'''

import os
from sayhello import app

dev_db = 'sqlite:///' + os.path.join(os.path.dirname(app.root_path), 'data.db')

SECRET_KEY = os.getenv('SECRET_KEY', 'secret_key')
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL", dev_db)
