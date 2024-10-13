from marshmallow import Schema, fields

class ClientSchema(Schema):
    id = fields.Int(dump_only= True)
    name = fields.Str(required= True)
    social_status_id = fields.Int(required = True)
