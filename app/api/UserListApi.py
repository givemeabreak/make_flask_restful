from flask import jsonify, request
from flask_restful import Resource, fields, marshal
from flask_restful.fields import Nested

from app.models import User





class UserListApi(Resource):
    def get(self):
        user_fields = {
            'uid': fields.Integer,
            'uname': fields.String,
            'upassword': fields.String
        }

        resource_fields = {
            'status': fields.Integer,
            'data': fields.Nested(user_fields)
        }

        u = User.query.all()
        data = {
            'status':'200',
            'data':u
        }
        return marshal(data,resource_fields)

    def post(self):
        u = User()
        u.uname = request.form.get('username')
        u.upassword = request.form.get('password')
        u.save()

        user_fields = {
            'uid': fields.Integer,
            'uname': fields.String,
            'upassword': fields.String
        }

        resource_fields = {
            'status': fields.Integer,
            'data': fields.Nested(user_fields)
        }
        data = {
            'status':'201',
            'data':u
        }
        return marshal(data,resource_fields)

class UserApi(Resource):
    def get(self,id):
        u = User.query.get(id)
        if u:
            resource_fields = {
                'status':fields.String,
                'uid':fields.Integer,
                'password':fields.String,
                'uname':fields.String
            }
            data = {
                'status':'200',
                'uid':id,
                'uname':u.uname,
                'password':u.upassword
            }
            return marshal(data,resource_fields)
        return 'user not exist'