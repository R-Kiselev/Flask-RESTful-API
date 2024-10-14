from marshmallow import Schema, fields
from marshmallow import validates, ValidationError

class CitySchema(Schema):
    id = fields.Int(dump_only= True)
    name = fields.Str(required= True)

    @validates("name")
    def validate_name(self, value):
        if not value.isalpha():
            raise ValidationError("City name must contain only alphabetic characters.")