from resources.base import BaseObjectResource, BaseListResource
from models.social_status import SocialStatus
from schemas.social_status import SocialStatusSchema

class SocialStatusObjectResource(BaseObjectResource):
    model = SocialStatus
    schema = SocialStatusSchema()

class SocialStatusListResource(BaseListResource):
    model = SocialStatus
    schema = SocialStatusSchema()