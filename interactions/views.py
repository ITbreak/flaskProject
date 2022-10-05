# -*- coding = utf-8 -*-

from flask_restplus import Resource

from interactions.init import app, api, ns, db
from interactions.args_parse.args_parse import get_login_args, get_data_args
from interactions.db import users
from interactions.model.request_model import login_req_model, get_data_req_model
from interactions.model.response_model import login_resp_model, get_data_resp_model
from interactions.model.response_class import Response


@app.before_first_request
def init_db():
    return db.create_all()


@ns.route("/login")
class Test(Resource):

    @ns.expect(login_req_model(api))
    @ns.response(200, "success", login_resp_model(api))
    def post(self):
        """
        测试
        :return:
        """
        args = get_login_args.parse_args()
        username = args.get("username")
        password = args.get("password")
        if not all([username, password]):
            return Response.fail(False, code=201)

        user_info = users.select_by_name(username)
        print(user_info.password)
        if user_info and user_info.password == password:
            return Response.success(True)
        else:
            return Response.fail(False)


@ns.route("/get_data")
class GetData(Resource):

    @ns.expect(get_data_req_model(api))
    @ns.response(200, "success", get_data_resp_model(api))
    def post(self):
        """获取测试数据"""
        args = get_data_args.parse_args()
        size = args.get("size", 0)
        print()


if __name__ == '__main__':
    app.run()
