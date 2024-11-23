from marshmallow import Schema, fields, post_dump, post_load
from marshmallow import validates, ValidationError

from app.models.role import Role
from app.extensions import db


class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    email = fields.Email(required=True)
    password = fields.String(load_only=True, required=True)
    roles = fields.List(fields.String())

    @validates("roles")
    def validate_roles(self, value):
        for role_name in value:
            role = db.session.query(Role).filter_by(name=role_name).first()
            if not role:
                raise ValidationError(f"Role '{role_name}' does not exist.")
    # Should read about it and write by my own!!!
    @post_load
    def convert_names_to_Roles(self, data, **kwargs):
        """Converts role names to 'Role' objects after loading into the schema."""
        role_names = data.get("roles", [])
        data["roles"] = db.session.query(Role).filter(Role.name.in_(role_names)).all()
        return data

    @post_dump
    def convert_Roles_to_names(self, data, **kwargs):
        """Converts 'Role' objects into strings after serialization."""
        roles = data.get("roles", [])
        if isinstance(roles, list) and roles and isinstance(roles[0], Role):
            data["roles"] = [role.name for role in roles]
        return data