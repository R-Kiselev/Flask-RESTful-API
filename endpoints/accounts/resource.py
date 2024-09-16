from flask_restful import reqparse, fields
from endpoints.BaseResource import BaseResource
from .model import Account

class AccountResource(BaseResource):
    model = Account
    
    item_fields = {
        'id': fields.Integer,
        'balance': fields.Integer,
        'client_id': fields.Integer,
        'bank_id': fields.Integer
    }

    item_list_fields = {
        'table_name': fields.String,
        'total': fields.Integer,
        'items': fields.List(fields.Nested(item_fields))
    }

    args_parser = reqparse.RequestParser()
    args_parser.add_argument('id', type=int, help="Account id should be integer")
    args_parser.add_argument('balance', type=int, default = 0, help="Account balance should be integer")
    args_parser.add_argument('client_id', type=int, required = True, help="Client id cannot be empty")
    args_parser.add_argument('bank_id', type=int, required = True, help="Bank id cannot be empty")
