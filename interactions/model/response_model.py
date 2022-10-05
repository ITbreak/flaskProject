# --encoding = utf-8--
"""
    @Time  : 2022/1/8 19:32
    @Author: Chen Feng
    @File  : response_model.py
"""
from flask_restplus import fields


def login_resp_model(api):
    return api.model("test_resp_model", {
        "result": fields.String(example="success", description="状态")

    })


def get_data_resp_model(api):
    return api.model("test_resp_model", {
        "result": fields.String(example="success", description="状态")

    })
