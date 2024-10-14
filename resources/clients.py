from commons.base_resources import BaseObjectResource, BaseListResource
from models.client import Client
from schemas.client import ClientSchema

class ClientObjectRes(BaseObjectResource):
    model = Client
    schema = ClientSchema()

class ClientListRes(BaseListResource):
    model = Client
    schema = ClientSchema()