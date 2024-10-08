from flask_restful import reqparse, fields
from endpoints.base import Base
from models.social_status import SocialStatus

class SocialStatus(Base):
    model = SocialStatus
    
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
    args_parser.add_argument('id', type=int, help="Social status id should be integer")
    args_parser.add_argument('name', type=str, required=True, help="Social status name cannot be empty")    