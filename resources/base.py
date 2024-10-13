from flask import request
from flask_restful import Resource
from db_settings import db
from marshmallow import Schema
from commons.pagination import paginate

class BaseObjectResource(Resource):
    model = None
    schema = Schema

    def get(self, id=None):
        item = self.model.query.get_or_404(id, description=f'No {self.model.__name__.lower()} found matching the criteria')
        return self.schema.dump(item), 200
            
    def put(self, id=None):
        item = self.model.query.get_or_404(id, description=f'{self.model.__name__.lower()} does not exist')
        
        data = self.schema.load(request.json, partial=True)
        for key, value in data.items():
            setattr(item, key, value)

        db.session.commit()
        return {
            "msg": "item updated",
            "item": self.schema.dump(item)
        }, 200
           
    def delete(self, id=None):
        item = self.model.query.get_or_404(id, description=f'{self.model.__name__.lower()} does not exist')

        db.session.delete(item)
        db.session.commit()

        return {
            "msg" : "item deleted",
            "item" : self.schema.dump(item)
        }, 204
    
class BaseListResource(Resource):
    model = None
    schema = Schema

    def get(self):
        query = self.model.query        
        return paginate(query, self.schema)
    
    def post(self):
        data = self.schema.load(request.json)
        item = self.model(**data)

        db.session.add(item)
        db.session.commit()

        return {
            "msg" : "item created",
            "item" : self.schema.dump(item)
        }, 201