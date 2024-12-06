from functools import wraps

from flask import request
from flask_jwt_extended import jwt_required, get_jwt

from app.commons.base_resources import BaseObjectResource, BaseListResource
from app.models.account import Account
from app.api.schemas.account import AccountSchema
from app.commons.pagination import paginate
from app.auth.utils import user_roles_required


def check_user_access(func):
    @wraps
    def wrapper(*args, **kwargs):
        jwt = get_jwt()
        account_ids = jwt.get('account_ids')
        if kwargs.get('id') not in account_ids:
            return {'err': 'Access denied'}, 403

        return func(*args, **kwargs)
    return wrapper


class AccountObjectRes(BaseObjectResource):
    model = Account
    schema = AccountSchema()

    method_decorators = [
        check_user_access,
        user_roles_required('admin', 'user'),
        jwt_required()
    ]


class BankAccountListRes(BaseListResource):
    model = Account
    schema = AccountSchema()

    method_decorators = {
        'get': [user_roles_required('admin'), jwt_required()],
        'post': [user_roles_required('admin', 'user'), jwt_required()]
    }

    def get(self, bank_id=None):
        query = Account.query.filter(Account.bank_id == bank_id)
        return paginate(query, self.schema)

    def post(self, bank_id=None):
        jwt = get_jwt()
        req = request.json
        jwt_client_id = jwt.get('client_id')
        req_client_id = req.get('client_id')

        if jwt_client_id != req_client_id:
            return {'err': 'Access denied'}, 403

        req['bank_id'] = bank_id
        return super().post()


class ClientAccountListRes(BaseListResource):
    model = Account
    schema = AccountSchema()

    method_decorators = {
        'get': [user_roles_required('admin'), jwt_required()],
        'post': [user_roles_required('admin', 'user'), jwt_required()]
    }

    def get(self, client_id=None):
        query = Account.query.filter(Account.client_id == client_id)
        return paginate(query, self.schema)

    def post(self, client_id=None):
        jwt = get_jwt()
        jwt_client_id = jwt.get('client_id')

        if jwt_client_id != client_id:
            return {'err': 'Access denied'}, 403

        req = request.json
        req['client_id'] = client_id

        return super().post()
