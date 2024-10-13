from marshmallow import Schema, fields

class CardSchema(Schema):
    id = fields.Int(dump_only= True)
    balance = fields.Int()
    account_id = fields.Int(required = True)
