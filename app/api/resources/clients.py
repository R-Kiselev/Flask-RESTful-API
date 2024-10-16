from app.commons.base_resources import BaseObjectResource, BaseListResource
from app.models.client import Client
from app.api.schemas.client import ClientSchema

class ClientObjectRes(BaseObjectResource):
    model = Client
    schema = ClientSchema()

class ClientListRes(BaseListResource):
    model = Client
    schema = ClientSchema()