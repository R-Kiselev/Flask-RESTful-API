from functools import wraps

from flask import request
from flask_jwt_extended import jwt_required, get_jwt

from app.commons.base_resources import BaseObjectResource, BaseListResource
from app.models.client import Client
from app.api.schemas.client import ClientSchema
from app.auth.utils import user_roles_required


def check_user_access(func):
    """Check if the user has access to the client
    If client user_id is not in the jwt claim 'user_id', return 403
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        jwt = get_jwt()
        if kwargs.get('id') != jwt.get('client_id'):
            return {"error": "Access denied"}, 403
        
        return func(*args, **kwargs)
    return wrapper


class ClientObjectRes(BaseObjectResource):
    model = Client
    schema = ClientSchema()

    # Order of decorators is important.
    # The first decorator called is the last one in the list
    method_decorators = [
        check_user_access,
        user_roles_required('admin', 'user'),
        jwt_required()
    ]


class ClientListRes(BaseListResource):
    model = Client
    schema = ClientSchema()

    method_decorators = {
        'get' : [user_roles_required('admin'), jwt_required()],
        'post' : [user_roles_required('admin', 'user'), jwt_required()]
    }


    def post(self):
        if get_jwt().get('user_id') != request.json.get('user_id'):
            return {'err' : 'Access denied'}, 403
        
        return super().post()
