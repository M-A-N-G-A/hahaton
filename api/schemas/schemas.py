from marshmallow import fields, Schema


class UserSchema(Schema):
    '''Создание схемы пользователя.'''
    uid = fields.Int()
    username = fields.Str()
    image_file = fields.Str()
    email = fields.Str()
    description = fields.Str()
    accuracy = fields.Int()


class PostSchema(Schema):
    '''Создание схемы пользователя.'''
    pid = fields.Int()
    content = fields.Str()
    media = fields.Str()
    date_posted = fields.DateTime("iso")
    user_id = fields.Int()
    liked = fields.List(fields.String(), required=True)
    comments = fields.List(fields.String(), required=True)
    notifs = fields.List(fields.String(), required=True)


class RecomendationsSchema(Schema):
    '''Создание схемы рекомендаций для подписок.'''
    username = fields.Str()
    image_file = fields.Str()


class CommentsSchema(Schema):
    '''Создание схемы комментариев.'''
    cid = fields.Int()
    user_id = fields.Int()
    pid = fields.Int()
    content = fields.Str()
    date_posted = fields.DateTime("iso")
