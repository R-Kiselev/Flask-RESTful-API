from app.commons.base_resources import BaseObjectResource, BaseListResource
from app.models.account import Account
from app.api.schemas.account import AccountSchema

from flask_restful import Resource, request
from app.extensions import db
from app.commons.pagination import paginate


class AccountObjectRes(BaseObjectResource):
    model = Account
    schema = AccountSchema()


class BankAccountListRes(BaseListResource):
    model = Account
    schema = AccountSchema()
    
    def get(self, bank_id = None):
        query = Account.query.filter(Account.bank_id == bank_id)
        return paginate(query, self.schema)

    def post(self, bank_id = None):
        req = request.json
        req['bank_id'] = bank_id

        return super().post()


class ClientAccountListRes(BaseListResource):
    model = Account
    schema = AccountSchema()

    def get(self, client_id = None):
        query = Account.query.filter(Account.client_id == client_id)
        return paginate(query, self.schema)
    
    def post(self, client_id = None):
        req = request.json
        req['client_id'] = client_id

        return super().post()