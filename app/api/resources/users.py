from flask import request
from flask_jwt_extended import jwt_required

from app.commons.base_resources import BaseListResource, BaseObjectResource
from app.models.user import User
from app.api.schemas.user import UserSchema, CreateUserSchema
from app.auth.utils import user_roles_required


class UserObjectResource(BaseObjectResource):
    model = User
    schema = UserSchema()

    method_decorators = [user_roles_required('admin'), jwt_required()]


class UserListResource(BaseListResource):
    model = User

    method_decorators = [user_roles_required('admin'), jwt_required()]

    def get(self):
        self.schema = UserSchema(many=True)

        return super().get()

    def post(self):
        self.schema = CreateUserSchema()

        user_data = self.schema.dump(request.json)

        user = User.query.filter_by(email=user_data.get('email')).first()
        if user:
            return {
                'err': 'User already exists'
            }, 409

        return super().post()
