from app.commons.base_resources import BaseObjectResource, BaseListResource
from app.models.bank import Bank
from app.api.schemas.bank import BankSchema
from app.auth.utils import user_roles_required


class BankObjectRes(BaseObjectResource):
    model = Bank
    schema = BankSchema()

    method_decorators = {
        'get': [user_roles_required('admin', 'manager', 'user')],
        'put': [user_roles_required('admin', 'manager')],
        'delete': [user_roles_required('admin', 'manager')]
    }

class BankListRes(BaseListResource):
    model = Bank
    schema = BankSchema()

    method_decorators = {
        'get': [user_roles_required('admin', 'manager', 'user')],
        'post': [user_roles_required('admin', 'manager')]
    }