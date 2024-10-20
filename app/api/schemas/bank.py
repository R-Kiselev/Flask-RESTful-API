from marshmallow import Schema, fields
from marshmallow import validates, ValidationError
import re

class BankSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)

    @validates("name")
    def validate_name(self, value):
        if not re.match(r"^[A-Za-z\s\-']+$", value):
            raise ValidationError("Bank name must contain only alphabetic characters, spaces, hyphens, and apostrophes.")
