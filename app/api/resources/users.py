from flask import request

from app.commons.base_resources import BaseListResource, BaseObjectResource
from app.models.user import User
from app.api.schemas.user import GetUserSchema, CreateUserSchema, UpdateUserSchema
from app.auth.utils import user_roles_required


class UserObjectResource(BaseObjectResource):
    model = User

    method_decorators = [user_roles_required('admin')]


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

    method_decorators = [user_roles_required('admin')]


    def get(self):
        self.schema = GetUserSchema(many=True)

        return super().get()


    def post(self):
        self.schema = CreateUserSchema()

        request_data = request.json
        request_data['roles'] = ['user']

        return super().post()
    