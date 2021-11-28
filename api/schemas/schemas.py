from marshmallow import Schema, fields

# TODO: ADD SCHEMAS!!!


class UserSchema(Schema):

    # Schema parameters.
    uid = fields.Int()
    username = fields.Str()
    image_file = fields.Str()
    email = fields.Str()	 
    image_file = fields.Str()	 
    description = fields.Str()	 
    accuracy = fields.Int()

class PostSchema(Schema):

    # Schema parameters.
    content = fields.Str()
    media = fields.Str()
    date_posted = fields.DateTime("iso")	 
    user_id = fields.Int()	 
    liked = fields.List(fields.String(), required=True)	 
    comments = fields.List(fields.String(), required=True)
    notifs = fields.List(fields.String(), required=True)

class RecomendationsSchema(Schema):

    # Schema parameters.
    username = fields.Str()
    image_file = fields.Str()

class CommentsSchema(Schema):

    # Schema parameters.
    user_id = fields.Int()
    pid = fields.Int()
    content = fields.Str()
    date_posted = fields.DateTime("iso")
