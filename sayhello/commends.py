#!/usr/bin/env python
# encoding: utf-8

'''
@author: lining
@file: commends.py
@time: 2020/11/5 22:58
@desc: 自定义flask命令
'''

import click
from sayhello import app, db
from sayhello.model import Message


@app.cli.command()
@click.option('--count', default=20, help='xxxxx')
def forge(count):
    from faker import Faker
    db.drop_all()
    db.create_all()

    fake = Faker()
    click.echo("working...")

    for i in range(count):
        message = Message(
            name=fake.name(),
            body=fake.sentence(),
            timestrap=fake.date_time_this_year()
        )
        db.session.add(message)
    db.session.commit()

    click.echo("Done .....")