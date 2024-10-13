from marshmallow import Schema, fields

class BranchSchema(Schema):
    id = fields.Int(dump_only= True)
    bank_id = fields.Int(required = True)
    city_id = fields.Int(required = True)
