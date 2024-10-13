from flask_restful import reqparse, fields
from resources.base import BaseObjectResource
from models.client import Client

class ClientResource(BaseObjectResource):
    model = Client
    
    item_fields = {
        'id': fields.Integer,
        'name': fields.String,
        'social_status_id': fields.Integer
    }

    item_list_fields = {
        'table_name': fields.String,
        'total': fields.Integer,
        'items': fields.List(fields.Nested(item_fields))
    }

    args_parser = reqparse.RequestParser()
    args_parser.add_argument('id', type=int, help="Client id should be integer")
    args_parser.add_argument('name', type=str, required=True, help="Client name cannot be empty")  
    args_parser.add_argument('social_status_id', type=int, required = True, help="Social status id should be integer")
