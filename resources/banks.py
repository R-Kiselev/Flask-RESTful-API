from flask_restful import reqparse, fields
from resources.base import Base
from models.bank import Bank

class Bank(Base):
    model = Bank
    
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
    args_parser.add_argument('id', type=int, help="Bank id should be integer")
    args_parser.add_argument('name', type=str, required=True, help="Bank name cannot be empty")    