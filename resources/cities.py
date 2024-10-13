from resources.base import BaseObjectResource, BaseListResource
from models.city import City
from schemas.city import CitySchema

class CityObjectResource(BaseObjectResource):
    model = City
    schema = CitySchema()

class CityListResource(BaseListResource):
    model = City
    schema = CitySchema()