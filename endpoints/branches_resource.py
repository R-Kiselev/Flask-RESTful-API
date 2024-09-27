from flask_restful import reqparse, fields
from endpoints.base_resource import BaseResource
from models.branch_model import Branch

class BranchResource(BaseResource):
    model = Branch
    
    item_fields = {
        'id': fields.Integer,
        'bank_id': fields.Integer,
        'city_id': fields.Integer
    }

    item_list_fields = {
        'table_name': fields.String,
        'total': fields.Integer,
        'items': fields.List(fields.Nested(item_fields))
    }

    args_parser = reqparse.RequestParser()
    args_parser.add_argument('id', type=int, help="Branch id should be integer")
    args_parser.add_argument('bank_id', type=int, required=True, help="Bank id cannot be empty")
    args_parser.add_argument('city_id', type=int, required=True, help="City id cannot be empty")   