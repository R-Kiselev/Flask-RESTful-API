from commons.base_resources import BaseObjectResource, BaseListResource
from models.bank import Bank
from schemas.bank import BankSchema

class BankObjectRes(BaseObjectResource):
    model = Bank
    schema = BankSchema()

class BankListRes(BaseListResource):
    model = Bank
    schema = BankSchema()