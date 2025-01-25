from flask import request
from flask_jwt_extended import jwt_required, get_jwt

from app.commons.base_resources import BaseObjectResource, BaseListResource
from app.commons.constants import ACCESS_DENIED_ERROR
from app.models.account import Account
from app.api.schemas.account import AccountSchema
from app.commons.pagination import paginate
from app.auth.utils import user_roles_required


def check_account_access(jwt, account_id):
    account_ids = jwt.get('account_ids')
    return account_id in account_ids


class AccountObjectRes(BaseObjectResource):
    model = Account
    schema = AccountSchema()

    method_decorators = [user_roles_required('admin', 'user'), jwt_required()]

    def get(self, id):
        if not check_account_access(get_jwt(), id):
            return ACCESS_DENIED_ERROR

        return super().get(id)

    def put(self, id):
        if not check_account_access(get_jwt(), id):
            return ACCESS_DENIED_ERROR

        return super().put(id)

    def delete(self, id):
        if not check_account_access(get_jwt(), id):
            return ACCESS_DENIED_ERROR

        return super().delete(id)


class AccountListRes(BaseListResource):
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
            return ACCESS_DENIED_ERROR

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
            return ACCESS_DENIED_ERROR

        req = request.json
        req['client_id'] = client_id

        return super().post()
