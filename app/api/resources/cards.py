from functools import wraps

from flask_restful import request
from flask_jwt_extended import jwt_required, get_current_user, get_jwt

from app.commons.base_resources import BaseObjectResource, BaseListResource
from app.models.card import Card
from app.api.schemas.card import CardSchema
from app.extensions import db
from app.commons.pagination import paginate
from app.auth.utils import user_roles_required


def check_user_access(func):
    """Check if the user has access to the card
    If card account_id is not in the jwt claim 'account_ids', return 403
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        jwt = get_jwt()
        card = db.session.query(Card).where(
            Card.id == kwargs.get('id')).first()
        if not card:
            return {"error": "Card not found"}, 404
        if card.account_id not in jwt.get('account_ids'):
            return {"error": "Access denied"}, 403

        return func(*args, **kwargs)
    return wrapper


class CardObjectRes(BaseObjectResource):
    model = Card
    schema = CardSchema()

    # Order of decorators is important.
    # The first decorator called is the last one in the list
    method_decorators = [
        check_user_access,
        user_roles_required('admin', 'user'),
        jwt_required()
    ]


class AccountCardListRes(BaseListResource):
    model = Card
    schema = CardSchema()

    method_decorators = {
        'get': [user_roles_required('admin'), jwt_required()],
        'post': [user_roles_required('admin', 'user'), jwt_required()]
    }

    def get(self, account_id=None):
        query = Card.query.filter(Card.account_id == account_id)

        return paginate(query, self.schema)

    def post(self, account_id=None):
        jwt = get_jwt()

        if account_id not in jwt.get('account_ids'):
            return {"error": "Access denied"}, 403

        req = request.json
        req['account_id'] = account_id

        return super().post()
