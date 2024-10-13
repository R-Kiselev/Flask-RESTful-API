from flask_restful import reqparse, fields
from resources.base import BaseObjectResource
from models.city import City

class CityResource(BaseObjectResource):
    model = City
    
    item_fields = {
        'id': fields.Integer,
        'name': fields.String
    }

    item_list_fields = {
        'table_name': fields.String,
        'total': fields.Integer,
        'items': fields.List(fields.Nested(item_fields))
    }

    args_parser = reqparse.RequestParser()
    args_parser.add_argument('id', type=int, help="City id should be integer")
    args_parser.add_argument('name', type=str, required=True, help="City name cannot be empty")  