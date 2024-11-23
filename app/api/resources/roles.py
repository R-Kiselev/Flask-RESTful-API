from app.commons.base_resources import BaseListResource, BaseObjectResource
from app.models.role import Role
from app.api.schemas.role import RoleSchema


class RoleObjectRes(BaseObjectResource):
    model = Role
    schema = RoleSchema()

class RoleListRes(BaseListResource):
    model = Role
    schema = RoleSchema()
