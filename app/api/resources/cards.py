from app.commons.base_resources import BaseObjectResource, BaseListResource
from app.models.card import Card
from app.api.schemas.card import CardSchema

from flask_restful import request
from app.extensions import db
from app.commons.pagination import paginate

class CardObjectRes(BaseObjectResource):
    model = Card
    schema = CardSchema()


class AccountCardListRes(BaseListResource):
    model = Card
    schema = CardSchema()

    def get(self, account_id = None):
        query = Card.query.filter(Card.account_id == account_id)
        return paginate(query, self.schema)
    
    def post(self, account_id = None):
        req = request.json
        req['account_id'] = account_id

        return super().post()