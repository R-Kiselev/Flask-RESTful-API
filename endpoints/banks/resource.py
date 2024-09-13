from flask_restful import Resource, request, reqparse
from flask_restful import fields, marshal, marshal_with
from .model import Bank
from settings import db

bank_fields = {
    'id': fields.Integer,
    'name': fields.String
}

bank_list_fields = {
    'total': fields.Integer,
    'banks': fields.List(fields.Nested(bank_fields))
}

args_parser = reqparse.RequestParser()
args_parser.add_argument('id', type=int, help="Bank id should be integer")
args_parser.add_argument('name', type=str, required=True, help="Bank name cannot be empty")

class BanksResource(Resource):
    def get(self, bank_id = None):
        if bank_id:
            bank = Bank.query.filter_by(id=bank_id).first()
            return marshal(bank, bank_fields)
        else:
            request_args = request.args.to_dict()
            limit = request_args.get('limit', 0)
            offset = request_args.get('offset', 0)

            request_args.pop('limit', None)
            request_args.pop('offset', None)

            banks = Bank.query.filter_by(**request_args)

            if limit:
                banks = banks.limit(limit)
            if offset:
                banks = banks.offset(offset)
            
            banks = banks.all()
            return marshal({
                'total': len(banks),
                'banks': marshal([bank for bank in banks], bank_fields)
            }, bank_list_fields)

    @marshal_with(bank_fields)
    def post(self):      
        args = args_parser.parse_args()
        bank = Bank(**args)

        db.session.add(bank)
        db.session.commit()

        return bank
    
    @marshal_with(bank_fields)
    def put(self, bank_id = None):
        bank = Bank.query.get_or_404(bank_id)

        if 'id' in request.get_json():
            bank.id = request.json['id']
        if 'name' in request.get_json():
            bank.name = request.json['name']

        db.session.commit()

        return bank
    