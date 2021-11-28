#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask_restful import Api

from api.handlers.handlers import (Index, UserData, PostData, PostsData,
    RecomendationsData, CommentsData, Login, FinanceData)


def generate_routes(app):

    # Create api
    api = Api(app)

    api.add_resource(Index, "/")
    api.add_resource(UserData, "/api/v1/users/<string:username>/")
    api.add_resource(PostData, "/api/v1/posts/<string:username>/")
    api.add_resource(PostsData, "/api/v1/followed/posts/<string:username>/")
    api.add_resource(RecomendationsData, "/api/v1/recomendations/<string:username>/")
    api.add_resource(CommentsData, "/api/v1/comments/<int:id>/")
    api.add_resource(Login, "/api/v1/login")
    api.add_resource(FinanceData, "/api/v1/tickers/<string:username>/")
