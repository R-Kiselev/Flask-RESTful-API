from flask_restful import Resource, request, reqparse, abort
from flask_restful import fields, marshal
from settings import db
from sqlalchemy.exc import IntegrityError

class BaseResource(Resource):
    model = None
    item_fields = {}
    item_list_fields = {}
    args_parser = None

    def get(self, id=None):
        if id:
            item = self.model.query.get_or_404(id, description=f'No {self.model.__name__.lower()} found matching the criteria')
            return marshal(item, self.item_fields)
        else:
            request_args = request.args.to_dict()
            limit = request_args.get('limit', 0)
            offset = request_args.get('offset', 0)

            request_args.pop('limit', None)
            request_args.pop('offset', None)

            items = self.model.query.filter_by(**request_args)

            if limit:
                items = items.limit(limit)
            if offset:
                items = items.offset(offset)

            items = items.all()
            if not items and (request_args or limit or offset):
                return abort(404, description=f'No {self.model.__name__.lower()} found matching the criteria')

            return marshal({
                'table_name': self.model.__name__,
                'total': len(items),
                'items': marshal([item for item in items], self.item_fields)
            }, self.item_list_fields)

    def post(self):
        args = self.args_parser.parse_args()
        if args['id']:
            existing_item = self.model.query.get(args['id'])
            if existing_item:
                abort(409, description=f'{self.model.__name__.lower()} with such id already exists')
        item = self.model(**args)

        db.session.add(item)
        try:
            db.session.commit()
        except IntegrityError as e:
            db.session.rollback()
            abort(400, description="Invalid foreign key, item does not exist")

        return marshal(item, self.item_fields)
    
    def put(self, id=None):
        item = self.model.query.get_or_404(id, description=f'{self.model.__name__.lower()} does not exist')
        for field in request.get_json():
            setattr(item, field, request.json[field])

        try:
            db.session.commit()
        except IntegrityError as e:
            db.session.rollback()
            abort(400, description="Invalid foreign key, item does not exist")

        return marshal(item, self.item_fields)
    
    def delete(self, id=None):
        item = self.model.query.get_or_404(id, description=f'{self.model.__name__.lower()} does not exist')

        db.session.delete(item)
        db.session.commit()

        return marshal(item, self.item_fields)