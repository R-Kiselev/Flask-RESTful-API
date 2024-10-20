from marshmallow import Schema, fields
from marshmallow import validates, ValidationError
import re

class CitySchema(Schema):
    id = fields.Int(dump_only= True)
    name = fields.Str(required= True)

    @validates("name")
    def validate_name(self, value):
        if not re.match(r"^[A-Za-z\s\-']+$", value):
            raise ValidationError("City name must contain only alphabetic characters, spaces, hyphens, and apostrophes.")