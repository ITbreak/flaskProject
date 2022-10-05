# --encoding = utf-8--
"""
    @Time  : 2021/8/19 23:01
    @Author: Chen Feng
    @File  : args_parse
"""
from flask_restplus import reqparse
parser = reqparse.RequestParser()


class RequestArg:
    def __init__(self, name: str, type_):
        self.name = name
        self.type = type_


def my_parser(_parser, args_list):
    parser_copy = _parser.copy()
    for args in args_list:
        parser_copy.add_argument(args.name, type=args.type, location="json")
    return parser_copy


get_login_args = my_parser(parser, [RequestArg("username", str),
                                    RequestArg("password", str)])

get_data_args = my_parser(parser, [RequestArg("size", float)])


if __name__ == '__main__':

    pass