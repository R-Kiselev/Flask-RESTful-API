from resources.base import BaseObjectResource, BaseListResource
from models.client import Client
from schemas.client import ClientSchema

class ClientObjectResource(BaseObjectResource):
    model = Client
    schema = ClientSchema()

class ClientListResource(BaseListResource):
    model = Client
    schema = ClientSchema()