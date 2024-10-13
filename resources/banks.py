from resources.base import BaseObjectResource, BaseListResource
from models.bank import Bank
from schemas.bank import BankSchema

class BankObjectResource(BaseObjectResource):
    model = Bank
    schema = BankSchema()

class BankListResource(BaseListResource):
    model = Bank
    schema = BankSchema()