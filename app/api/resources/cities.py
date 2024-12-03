from app.commons.base_resources import BaseObjectResource, BaseListResource
from app.models.city import City
from app.api.schemas.city import CitySchema
from app.auth.utils import user_roles_required


class CityObjectRes(BaseObjectResource):
    model = City
    schema = CitySchema()

    method_decorators = {
        'get': [user_roles_required('admin', 'manager', 'user')],
        'put': [user_roles_required('admin', 'manager')],
        'delete': [user_roles_required('admin', 'manager')]
    }

class CityListRes(BaseListResource):
    model = City
    schema = CitySchema()

    method_decorators = {
        'get': [user_roles_required('admin', 'manager', 'user')],
        'post': [user_roles_required('admin', 'manager')]
    }