from flask_jwt_extended import jwt_required

from app.commons.base_resources import BaseObjectResource, BaseListResource
from app.models.bank import Bank
from app.api.schemas.bank import BankSchema
from app.auth.utils import user_roles_required


class BankObjectRes(BaseObjectResource):
    model = Bank
    schema = BankSchema()

    method_decorators = {
        'get': [user_roles_required('admin', 'manager', 'user'), jwt_required()],
        'put': [user_roles_required('admin', 'manager'), jwt_required()],
        'delete': [user_roles_required('admin', 'manager'), jwt_required()]
    }

class BankListRes(BaseListResource):
    model = Bank
    schema = BankSchema()

    method_decorators = {
        'get': [user_roles_required('admin', 'manager', 'user'), jwt_required()],
        'post': [user_roles_required('admin', 'manager'), jwt_required()]
    }