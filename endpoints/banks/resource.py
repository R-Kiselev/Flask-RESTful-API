from flask_restful import Resource, request, reqparse
from flask_restful import fields, marshal, marshal_with
from .model import Bank
from settings import db

bank_fields = {
    'id': fields.Integer,
    'name': fields.String
}

args_parser = reqparse.RequestParser()
args_parser.add_argument('id', type=int, help="Bank id should be integer")
args_parser.add_argument('name', type=str, required=True, help="Bank name cannot be empty")

class BanksResource(Resource):
    @marshal_with(bank_fields)
    def get(self, bank_id = None):
        if bank_id:
            bank = Bank.query.filter_by(id=bank_id).first()
            return bank
    
    @marshal_with(bank_fields)
    def post(self):      
        args = args_parser.parse_args()
        bank = Bank(**args)

        db.session.add(bank)
        db.session.commit()

        return bank
