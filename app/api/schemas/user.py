from marshmallow import Schema, fields, validates, ValidationError, post_load

from app.models.role import Role
from app.extensions import db


class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    email = fields.Email(required=True)
    password = fields.String(load_only=True, required=True)
    roles = fields.List(fields.String(), required=True)
    is_blocked = fields.Bool()

    @validates("roles")
    def validate_roles(self, value):
        """Checks if roles exist in database."""
        for role_name in value:
            role = db.session.query(Role).filter_by(name=role_name).first()
            if not role:
                raise ValidationError(f"Role '{role_name}' does not exist.")

    @post_load
    def convert_names_to_roles(self, input_data, **kwargs):
        """Converts role names from strings to objects so sqlalchemy model can show users.roles.
        This function is called when loading data from json to python object."""
        if "roles" in input_data:
            role_objects = Role.query.filter(
                Role.name.in_(input_data['roles'])).all()
            input_data['roles'] = role_objects
        return input_data


# the Meta class helps customize each schema for their purposes
class GetUserSchema(UserSchema):
    class Meta:
        exclude = ("password",)


class CreateUserSchema(UserSchema):
    class Meta:
        load_only = ("password",)
        dump_only = ("is_blocked",)


class UpdateUserSchema(UserSchema):
    class Meta:
        exclude = ("password",)
