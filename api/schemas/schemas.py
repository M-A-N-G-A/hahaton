from marshmallow import Schema, fields

# TODO: ADD SCHEMAS!!!


class UserSchema(Schema):

    # Schema parameters.
    user_id = fields.Str()
    username = fields.Str()
    # password = fields.Str()
    image_file = fields.Str()
    email = fields.Str()	 
    image_file = fields.Str()	 
    description = fields.Str()	 
    accuracy = fields.Str()
    # role = fields.Str()

class PostSchema(Schema):

    # Schema parameters.
    content = fields.Str()
    media = fields.Str()
    date_posted = fields.Str()	 
    user_id = fields.Str()	 
    liked = fields.Str()	 
    comments = fields.Str()
    notifs = fields.Str()

class RecomendationsSchema(Schema):

    # Schema parameters.
    username = fields.Str()
    image_file = fields.Str()

class CommentsSchema(Schema):

    # Schema parameters.
    user_id = fields.Str()
    pid = fields.Str()
    content = fields.Str()
    date_posted = fields.Str()
