# --encoding = utf-8--
"""
    @Time  : 2022/1/9 22:20
    @Author: Chen Feng
    @File  : response_class.py
"""

class Response:

    @staticmethod
    def success(data, code=200):
        data = str(data)
        return {
            "message": "success",
            "code": code,
            "data": data
        }

    @staticmethod
    def fail(data, code=200):
        data = str(data)
        return {
            "message": "fail",
            "code": code,
            "data": data
        }
