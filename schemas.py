from marshmallow import Schema, fields


class GameSchema(Schema):
    id = fields.Int(dump_only=True)
    date = fields.Date(required=True)
    team_1 = fields.Str(required=True)
    team_2 = fields.Str(required=True)
    stadium = fields.Str(required=True)
