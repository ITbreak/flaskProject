# -*- coding = utf-8 -*-
import os
from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

from flask_restplus import Api, Namespace


app = Flask(__name__)


app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL", "sqlite:///" +
                                                  os.path.join(app.root_path, 'db', "data.db"))
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["ERROR_404_HELP"] = False
cors = CORS(app)
db = SQLAlchemy(app)


@app.route("/")
def index():
    return app.send_static_file("login.html")


api = Api(doc="/doc/")
api.init_app(app=app,
             title="title",
             description="description",
             terms_url="/terms_url",
             contact="793704058@qq.com",
             license="123456",
             license_url="/license_url")

ns = Namespace('Test', description='Test des', path='/cf/')
api.add_namespace(ns)





