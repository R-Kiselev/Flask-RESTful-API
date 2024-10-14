from marshmallow import Schema, fields
from marshmallow import validates, ValidationError

class CardSchema(Schema):
    id = fields.Int(dump_only= True)
    balance = fields.Int()
    account_id = fields.Int(required = True)

    @validates("balance")
    def validate_balance(self, value):
        if value < 0:
            raise ValidationError("Balance must be a positive integer.")

    @validates("account_id")
    def validate_account_id(self, value):
        if value <= 0:
            raise ValidationError("Account ID must be a positive integer.")