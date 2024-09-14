from flask_restful import Resource, request, reqparse, abort
from flask_restful import fields, marshal, marshal_with
from .model import Branch
from settings import db

branch_fields = {
    'id': fields.Integer,
    'bank_id': fields.Integer,
    'branch_id': fields.Integer
}

branch_list_fields = {
    'total': fields.Integer,
    'branches': fields.List(fields.Nested(branch_fields))
}

args_parser = reqparse.RequestParser()
args_parser.add_argument('id', type=int, help="Branch id should be integer")
args_parser.add_argument('bank_id', type=int, required=True, help="Bank id cannot be empty")
args_parser.add_argument('city_id', type=int, required=True, help="City id cannot be empty")

class BranchResource(Resource):
    def get(self, branch_id = None):
        if branch_id:
            branch = Branch.query.get_or_404(branch_id, description = "No branches found matching the criteria")
            return marshal(Branch, branch_fields)
        else:
            request_args = request.args.to_dict()
            limit = request_args.get('limit', 0)
            offset = request_args.get('offset', 0)

            request_args.pop('limit', None)
            request_args.pop('offset', None)

            branches = Branch.query.filter_by(**request_args)

            if limit:
                branches = branches.limit(limit)
            if offset:
                branches = branches.offset(offset)

            branches = branches.all()
            if not branches and (request_args or limit or offset):
                return abort(404, description = "No branches found matching the criteria")

            return marshal({
                'total': len(branches),
                'branches': marshal([branch for branch in branches], branch_fields)
            }, branch_list_fields)

    @marshal_with(branch_fields)
    def post(self):  
        args = args_parser.parse_args()
        if args['id']:
            existing_branch = Branch.query.get(args['id'])
            if existing_branch:
                abort(409, description = "Branch with such id already exists")
        branch = Branch(**args)

        db.session.add(branch)
        db.session.commit()

        return branch
    
    @marshal_with(branch_fields)
    def put(self, branch_id = None):
        branch = Branch.query.get_or_404(branch_id, description= 'Branch does not exist')

        if 'id' in request.get_json():
            branch.id = request.json['id']
        if 'name' in request.get_json():
            branch.name = request.json['name']

        db.session.commit()

        return branch
    
    @marshal_with(branch_fields)
    def delete(self, branch_id = None):
        branch = Branch.query.get_or_404(branch_id, description= 'Branch does not exist')

        db.session.delete(branch)
        db.session.commit()

        return branch