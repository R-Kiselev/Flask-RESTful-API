from app.commons.base_resources import BaseObjectResource, BaseListResource
from app.models.card import Card
from app.api.schemas.card import CardSchema

from flask_restful import request
from app.extensions import db
from app.commons.pagination import paginate
from app.auth.utils import user_roles_required


class CardObjectRes(BaseObjectResource):
    model = Card
    schema = CardSchema()

    method_decorators = {
        'get': [user_roles_required('admin', 'manager', 'user')],
        'put': [user_roles_required('admin', 'manager')],
        'delete': [user_roles_required('admin', 'manager')]
    }


class AccountCardListRes(BaseListResource):
    model = Card
    schema = CardSchema()

    method_decorators = {
        'get': [user_roles_required('admin', 'manager', 'user')],
        'post': [user_roles_required('admin', 'manager')]
    }

    def get(self, account_id = None):
        query = Card.query.filter(Card.account_id == account_id)
        return paginate(query, self.schema)
    
    def post(self, account_id = None):
        req = request.json
        req['account_id'] = account_id

        return super().post()