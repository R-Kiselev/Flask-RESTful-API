from app.commons.base_resources import BaseObjectResource, BaseListResource
from app.models.social_status import SocialStatus
from app.api.schemas.social_status import SocialStatusSchema
from app.auth.utils import user_roles_required

class SocialStatusObjectRes(BaseObjectResource):
    model = SocialStatus
    schema = SocialStatusSchema()

    method_decorators = {
        'get' : [user_roles_required('admin', 'manager', 'user')],
        'all' : [user_roles_required('admin', 'manager')], 
    }


class SocialStatusListRes(BaseListResource):
    model = SocialStatus
    schema = SocialStatusSchema()

    method_decorators = {
        'get' : [user_roles_required('admin', 'manager', 'user')],
        'post': [user_roles_required('admin', 'manager')]
    }
