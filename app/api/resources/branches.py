from app.commons.base_resources import BaseObjectResource, BaseListResource
from app.models.branch import Branch
from app.api.schemas.branch import BranchSchema

from flask_restful import Resource, request
from app.extensions import db
from app.commons.pagination import paginate


class BranchObjectRes(BaseObjectResource):
    model = Branch
    schema = BranchSchema()


class BranchListRes(BaseListResource):
    schema = BranchSchema()

    def get(self, bank_id = None):
        query = Branch.query.filter(Branch.bank_id == bank_id)
        return paginate(query, self.schema)
    
    def post(self, bank_id = None):
        req = request.json
        req['bank_id'] = bank_id
        
        return super().post()