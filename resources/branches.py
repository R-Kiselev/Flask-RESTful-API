from resources.base import BaseObjectResource, BaseListResource
from models.branch import Branch
from schemas.branch import BranchSchema

class BranchObjectResource(BaseObjectResource):
    model = Branch
    schema = BranchSchema()

class BranchListResource(BaseListResource):
    model = Branch
    schema = BranchSchema()