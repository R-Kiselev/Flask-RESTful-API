from flask_restful import reqparse, fields
from endpoints.base import Base
from models.card import Card

class Card(Base):
    model = Card
    
    item_fields = {
        'id': fields.Integer,
        'balance': fields.Integer,
        'account_id': fields.Integer,
    }

    item_list_fields = {
        'table_name': fields.String,
        'total': fields.Integer,
        'items': fields.List(fields.Nested(item_fields))
    }

    args_parser = reqparse.RequestParser()
    args_parser.add_argument('id', type=int, help="Card id should be integer")
    args_parser.add_argument('balance', type=int, default = 0, help="Card balance should be integer")
    args_parser.add_argument('account_id', type=int, required = True, help="Account id cannot be empty")

