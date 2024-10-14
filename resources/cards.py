from commons.base_resources import BaseObjectResource, BaseListResource
from models.card import Card
from schemas.card import CardSchema

from flask_restful import Resource, request
from db_settings import db
from commons.pagination import paginate

class CardObjectResource(BaseObjectResource):
    model = Card
    schema = CardSchema()

class CardListResource(BaseListResource):
    model = Card
    schema = CardSchema()

class CardsAccountResource(Resource):
    schema = CardSchema()

    def get(self, account_id = None):
        query = Card.query.filter(Card.account_id == account_id)
        return paginate(query, self.schema)
    
    def post(self, account_id = None):
        req = request.json
        req['account_id'] = account_id

        data = self.schema.load(request.json)
        item = Card(**data)

        db.session.add(item)
        db.session.commit()

        return {
            "msg" : "item created",
            "item" : self.schema.dump(item)
        }, 201