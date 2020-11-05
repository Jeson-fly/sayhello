#!/usr/bin/env python
# encoding: utf-8

'''
@author: lining
@file: views.py
@time: 2020/11/5 22:57
@desc: 视图函数
'''
from flask import request, render_template, redirect, flash, url_for

from sayhello import app, db
from sayhello.model import Message
from sayhello.forms import HelloForm


@app.route("/", methods=["GET", "POST"])
def index():
    form = HelloForm()
    message = Message.query.order_by(Message.timestamp.desc()).all()
    if form.validate_on_submit():
        name = form.name.data
        body = form.body.data
        message = Message(name=name,body=body)
        db.session.add(message)
        db.session.commit()
        flash("You message have been sent to the world")
        return redirect(url_for('index'))
    return render_template("index.html", form=form, message=message)
