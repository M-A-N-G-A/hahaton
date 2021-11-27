import logging
from datetime import datetime

from flask import g, request, jsonify

from flask_restful import Resource


import api.errors.errors as error


from api.database.database import db
from api.models.models import User, Post
from api.schemas.schemas import UserSchema, PostSchema, RecomendationsSchema





class Index(Resource):
    @staticmethod
    def get():
        return "Hello world"


class UserData(Resource):
    def get(self, username):
        user = User.query.filter_by(username=username)

        # create user schema for serializing
        user_schema = UserSchema(many=True)

        # get json data
        data = user_schema.dump(user)

        # return json from db
        print(data)
        return data

class PostData(Resource):
    def get(self, username):
        user = User.query.filter_by(username=username).first()
        posts = Post.query.filter_by(user_id=user.uid)

        # create user schema for serializing
        post_schema = PostSchema(many=True)

        # get json data
        data = post_schema.dump(posts)

        # return json from db
        print(data)
        return data


class RecomendationsData(Resource):
    def get(self, username):
        recomendations = User.get_user_suggestion(username)

        # create user schema for serializing
        recomendations_schema = RecomendationsSchema(many=True)

        # get json data

        data = recomendations_schema.dump(recomendations)

        # return json from db
        print(data)
        return data

    def post(self, username):
        follow = User.is_following(username)
        if not follow:
            User.follow(username)
    
        return '', 200

