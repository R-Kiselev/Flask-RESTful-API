from flask_restful import Resource, request, reqparse
from flask_restful import fields, marshal, marshal_with
from banks import model
from app import db

bank_fields = {
    'id': fields.Integer,
    'name': fields.String
}

args_parser = reqparse.RequestParser()
args_parser.add_argument(key='id', type=int, help="Bank id should be integer")
args_parser.add_argument(key='name', type=str, required=True, help="Bank name cannot be empty")

class BanksResource(Resource):
    @marshal_with(bank_fields)
    def get(self, bank_id = None):
        if bank_id:
            bank = model.Bank.query.filter_by(id=bank_id).first()
            return bank
    
    @marshal_with(bank_fields)
    def post(self, bank_id):
        args = args_parser.parse_args()
        bank = model.Bank(**args)

        db.session.add(bank)
        db.session.commit()

        return bank
