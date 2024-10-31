from app.commons.base_resources import BaseObjectResource, BaseListResource
from app.models.city import City
from app.api.schemas.city import CitySchema

class CityObjectRes(BaseObjectResource):
    model = City
    schema = CitySchema()

class CityListRes(BaseListResource):
    model = City
    schema = CitySchema()