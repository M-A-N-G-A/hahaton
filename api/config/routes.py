#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask_restful import Api

from api.handlers.handlers import Index, UserData, Matrix


def generate_routes(app):

    # Create api
    api = Api(app)

    api.add_resource(Index, "/")
    api.add_resource(UserData, "/api/v1/users/<string:username>")
    #api.add_resource(Matrix, "/matrix")
    # api.add_resource(UserData, "/api/v1/users/<string:username>")