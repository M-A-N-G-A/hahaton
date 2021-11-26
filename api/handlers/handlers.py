import logging
from datetime import datetime

from flask import g, request, jsonify

from flask_restful import Resource


import api.errors.errors as error

from api.tmdb.tmdb import TMDB
from api.database.database import db
from api.models.models import User, Post
from api.schemas.schemas import UserSchema, PostSchema


WRAPPER = TMDB()


class Index(Resource):
    @staticmethod
    def get():
        return "Hello world"


# class UsersData(Resource):
#     def get(self):
#         users = User.query.all()

#         # create user schema for serializing
#         user_schema = UserSchema(many=True)

#         # get json data
#         data = user_schema.dump(users)

#         # return json from db
#         return data


class Matrix(Resource):
    def get(self):
        return jsonify(WRAPPER.search_movie_by_name("matrix"))

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
