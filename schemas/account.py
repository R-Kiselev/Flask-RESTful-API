from marshmallow import Schema, fields

class AccountSchema(Schema):
    id = fields.Int(dump_only= True)
    balance = fields.Int()
    client_id = fields.Int(required = True)
    bank_id = fields.Int(required = True)
