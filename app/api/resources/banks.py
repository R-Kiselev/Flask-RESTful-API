from app.commons.base_resources import BaseObjectResource, BaseListResource
from app.models.bank import Bank
from app.api.schemas.bank import BankSchema

class BankObjectRes(BaseObjectResource):
    model = Bank
    schema = BankSchema()

class BankListRes(BaseListResource):
    model = Bank
    schema = BankSchema()