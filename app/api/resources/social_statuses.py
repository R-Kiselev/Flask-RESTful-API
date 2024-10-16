from app.commons.base_resources import BaseObjectResource, BaseListResource
from app.models.social_status import SocialStatus
from app.api.schemas.social_status import SocialStatusSchema

class SocialStatusObjectRes(BaseObjectResource):
    model = SocialStatus
    schema = SocialStatusSchema()

class SocialStatusListRes(BaseListResource):
    model = SocialStatus
    schema = SocialStatusSchema()