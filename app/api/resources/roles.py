from app.commons.base_resources import BaseListResource, BaseObjectResource
from app.models.role import Role
from app.api.schemas.role import RoleSchema
from app.auth.utils import user_roles_required


class RoleObjectRes(BaseObjectResource):
    model = Role
    schema = RoleSchema()

    method_decorators = [user_roles_required('admin')]

class RoleListRes(BaseListResource):
    model = Role
    schema = RoleSchema()

    method_decorators = [user_roles_required('admin')]
