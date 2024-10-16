from marshmallow import Schema, fields
from marshmallow import validates, ValidationError

class SocialStatusSchema(Schema):
    id = fields.Int(dump_only= True)
    name = fields.Str(required= True)
    
    @validates("name")
    def validate_name(self, value):
        if not value.isalpha():
            raise ValidationError("Social status name must contain only alphabetic characters.")