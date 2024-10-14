from marshmallow import Schema, fields
from marshmallow import validates, ValidationError

class AccountSchema(Schema):
    id = fields.Int(dump_only= True)
    balance = fields.Int()
    client_id = fields.Int(required = True, dump_only = True)
    bank_id = fields.Int(required = True, dump_only = True)

    @validates("balance")
    def validate_balance(self, value):
        if value < 0:
            raise ValidationError("Balance must be a positive integer.")