from flask_restful import Api
from app.api.UserListApi import UserListApi, UserApi

api = Api()

def init_api(app):
    api.init_app(app)


api.add_resource(UserListApi,'/users/')
api.add_resource(UserApi,'/user/<int:id>/')