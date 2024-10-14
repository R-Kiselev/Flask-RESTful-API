from commons.base_resources import BaseObjectResource, BaseListResource
from models.city import City
from schemas.city import CitySchema

class CityObjectRes(BaseObjectResource):
    model = City
    schema = CitySchema()

class CityListRes(BaseListResource):
    model = City
    schema = CitySchema()