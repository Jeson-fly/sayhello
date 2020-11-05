#!/usr/bin/env python
# encoding: utf-8

'''
@author: lining
@file: __init__.py
@time: 2020/11/5 22:37
@desc:
'''
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_moment import Moment


app = Flask("sayhello")
app.config.from_pyfile('settings.py')  # 加载配置文件
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True

db = SQLAlchemy(app)
bootstrap = Bootstrap(app)
moment=Moment(app)

@app.route("/")
def index():
    return "hello"


from sayhello import views, errors, commends

if __name__ == "__main__":
    app.run(debug=True)
