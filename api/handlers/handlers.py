import logging
from datetime import datetime

from flask import g, request, jsonify

from flask_restful import Resource


import api.errors.errors as error

from api.tmdb.tmdb import TMDB
from api.database.database import db
from api.models.models import User
from api.schemas.schemas import UserSchema


WRAPPER = TMDB()


class Index(Resource):
    @staticmethod
    def get():
        return "Hello world"


class UsersData(Resource):
    def get(self):
        users = User.query.all()

        # create user schema for serializing
        user_schema = UserSchema(many=True)

        # get json data
        data = user_schema.dump(users)

        # return json from db
        return data


class Matrix(Resource):
    def get(self):
        return jsonify(WRAPPER.search_movie_by_name("matrix"))
