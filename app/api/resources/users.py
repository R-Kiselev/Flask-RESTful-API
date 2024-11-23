import os

from flask import request, jsonify
from dotenv import load_dotenv

from app.commons. base_resources import BaseListResource, BaseObjectResource
from app.models.user import User
from app.models.role import Role
from app.api.schemas.user import UserSchema
from app.extensions import db


load_dotenv()

DEFAULT_ROLE_NAME = os.getenv('DEFAULT_ROLE')

class UserObjectResource(BaseObjectResource):
    model = User
    schema = UserSchema()


class UserListResource(BaseListResource):
    model = User
    schema = UserSchema()

    def post(self):
        req = request.json
        req['roles'] = [DEFAULT_ROLE_NAME]

        return super().post()
    