# -*- coding = utf-8 -*-
"""
    Time    : 2021/8/7 22:47
    Author  : CF
    File    : users.py
    Software: Pycharm
"""
from flask import flash

from interactions.init import db


class Users(db.Model):

    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True)
    password = db.Column(db.String)

    def __repr__(self):
        return 'username:%s' % self.name

    def to_dict(self):
        return {
            'username': self.username,
            'password': self.password
        }


def add(user_info: dict):
    """
    func:添加数据
    :param user_info:
    :return:
    """
    db.session.add(Users(username=user_info.get("username"),
                          password=user_info.get("password")
                          ))
    return db.session.commit()


def delete(id: int):
    """
    delete by id
    :param id:
    :return:
    """
    author = Users.query.get(id)
    if author:
        try:
            db.session.delete(author)
            db.session.commit()
        except Exception as e:
            print(e)
            flash('操作失败')
            db.session.rollback()
    else:
        flash('数据不存在')


def select_by_name(username: str):
    """
    select by name
    :param username:
    :return:
    """
    return Users.query.filter(Users.username == username).first()
