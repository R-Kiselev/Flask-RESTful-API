from marshmallow import Schema, fields
from marshmallow import validates, ValidationError
import re
class ClientSchema(Schema):
    id = fields.Int(dump_only= True)
    name = fields.Str(required= True)
    social_status_id = fields.Int(required = True)
    
    @validates("name")
    def validate_name(self, value):
        if not re.match(r"^[A-Za-z\s\-']+$", value):
            raise ValidationError("Client name must contain only alphabetic characters, spaces, hyphens, and apostrophes.")
    
    @validates("social_status_id")
    def validate_social_status_id(self, value):
        if value <= 0:
            raise ValidationError("Social Status ID must be a positive integer.")