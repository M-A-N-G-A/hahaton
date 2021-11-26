from marshmallow import Schema, fields

# TODO: ADD SCHEMAS!!!


class UserSchema(Schema):

    # Schema parameters.
    username = fields.Str()
    password = fields.Str()
    image_file = fields.Str()
