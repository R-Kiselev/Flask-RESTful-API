from commons.base_resources import BaseObjectResource, BaseListResource
from models.social_status import SocialStatus
from schemas.social_status import SocialStatusSchema

class SocialStatusObjectRes(BaseObjectResource):
    model = SocialStatus
    schema = SocialStatusSchema()

class SocialStatusListRes(BaseListResource):
    model = SocialStatus
    schema = SocialStatusSchema()