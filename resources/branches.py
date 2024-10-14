from commons.base_resources import BaseObjectResource
from models.branch import Branch
from schemas.branch import BranchSchema

from flask_restful import Resource, request
from db_settings import db
from commons.pagination import paginate


class BankBranchObjectRes(BaseObjectResource):
    model = Branch
    schema = BranchSchema()


class BankBranchListRes(Resource):
    schema = BranchSchema()

    def get(self, bank_id = None):
        query = Branch.query.filter(Branch.bank_id == bank_id)
        return paginate(query, self.schema)
    
    def post(self, bank_id = None):
        req = request.json
        req['bank_id'] = bank_id

        data = self.schema.load(request.json)
        item = Branch(**data)

        db.session.add(item)
        db.session.commit()

        return {
            "msg" : "item created",
            "item" : self.schema.dump(item)
        }, 201