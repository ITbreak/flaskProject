# --encoding = utf-8--
"""
    @Time  : 2021/8/18 21:06
    @Author: Chen Feng
    @File  : request_model
"""
from flask_restplus import fields


def login_req_model(api):
    return api.model("login_req_model", {"username": fields.Integer(example=123, description="test"),
                                         "password": fields.Integer(example=456, description="test")
                                         })


def get_data_req_model(api):
    return api.model("get_data_req_model", {"size": fields.Integer(example=100, description="数据量(k)")})
