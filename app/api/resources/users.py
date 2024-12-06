from flask import request
from flask_jwt_extended import jwt_required

from app.commons.base_resources import BaseListResource, BaseObjectResource
from app.models.user import User
from app.api.schemas.user import GetUserSchema, CreateUserSchema, UpdateUserSchema
from app.auth.utils import user_roles_required


class UserObjectResource(BaseObjectResource):
    model = User

    method_decorators = [user_roles_required('admin'), jwt_required()]


    def get(self, id):
        self.schema = GetUserSchema()

        return super().get(id)
    
    def put(self, id):
        self.schema = UpdateUserSchema()

        return super().put(id)
    
    def delete(self, id):
        self.schema = GetUserSchema()
        
        return super().delete(id)


class UserListResource(BaseListResource):
    model = User

    method_decorators = [user_roles_required('admin'), jwt_required()]


    def get(self):
        self.schema = GetUserSchema(many=True)

        return super().get()


    def post(self):
        self.schema = CreateUserSchema()

        request_data = request.json
        
        user_data = self.schema.dump(request_data)
        if User.query.filter_by(email = user_data.get('email')).first() :
            return {
                'err' : 'User already exists'
            }, 409

        request_data['roles'] = ['user']


        return super().post()
    