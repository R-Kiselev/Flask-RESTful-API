from resources.base import BaseObjectResource, BaseListResource
from models.account import Account
from schemas.account import AccountSchema

class AccountObjectResource(BaseObjectResource):
    model = Account
    schema = AccountSchema()

class AccountListResource(BaseListResource):
    model = Account
    schema = AccountSchema()