from resources.base import BaseObjectResource, BaseListResource
from models.card import Card
from schemas.card import CardSchema

class CardObjectResource(BaseObjectResource):
    model = Card
    schema = CardSchema()

class CardListResource(BaseListResource):
    model = Card
    schema = CardSchema()