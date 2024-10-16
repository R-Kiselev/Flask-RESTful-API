from marshmallow import Schema, fields
from marshmallow import validates, ValidationError

class BranchSchema(Schema):
    id = fields.Int(dump_only= True)
    bank_id = fields.Int(required = True)
    city_id = fields.Int(required = True)

    @validates("bank_id")
    def validate_bank_id(self, value):
        if value <= 0:
            raise ValidationError("Bank ID must be a positive integer.")
    
    @validates("city_id")
    def validate_city_id(self, value):
        if value <= 0:
            raise ValidationError("City ID must be a positive integer.")