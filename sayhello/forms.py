#!/usr/bin/env python
# encoding: utf-8

'''
@author: lining
@file: forms.py
@time: 2020/11/5 23:18
@desc: 表单类
'''
from flask_wtf import FlaskForm
import wtforms as wtf
from wtforms.validators import DataRequired, Length


class HelloForm(FlaskForm):
    name = wtf.StringField("name", validators=[DataRequired(), Length(1, 20)])
    body = wtf.TextAreaField("message", validators=[DataRequired(), Length(1, 200)])
    submit = wtf.SubmitField()
