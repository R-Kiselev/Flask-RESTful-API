from app.commons.base_resources import BaseObjectResource, BaseListResource
from app.models.client import Client
from app.api.schemas.client import ClientSchema
from app.auth.utils import user_roles_required


class ClientObjectRes(BaseObjectResource):
    model = Client
    schema = ClientSchema()

    method_decorators = [user_roles_required('admin', 'manager')]

class ClientListRes(BaseListResource):
    model = Client
    schema = ClientSchema()

    method_decorators = [user_roles_required('admin', 'manager')]
