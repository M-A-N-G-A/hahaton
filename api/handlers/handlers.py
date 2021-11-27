import logging
from datetime import datetime
from flask import g, request, jsonify
from flask_restful import Resource

import api.errors.errors as error


from api.database.database import db
from api.models.models import Comment, User, Post
from api.schemas.schemas import UserSchema, PostSchema, RecomendationsSchema, CommentsSchema


class Login(Resource):
    def post():
        content = request.json
        user = User.query.filter_by(
            username=content['username'],
            password=content['password'],
        )
        if user:
            user_schema = UserSchema(many=True)
            data = user_schema.dump(user)
            return data, 200
        return 'Неправильные логин или пароль', 401


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
        return data


class RecomendationsData(Resource):
    def get(self, username):
        user = User.query.filter_by(username=username).first()
        recomendations = user.get_user_suggestion()
        # create user schema for serializing
        recomendations_schema = RecomendationsSchema(many=True)
        # get json data
        data = recomendations_schema.dump(recomendations)
        # return json from db
        return data

    def post(self, username):
        uid = request.json['user_id']
        user = User.query.filter_by(uid=uid).first()
        user_following = User.query.filter_by(username=username).first()
        user.follow(user_following)
        db.session.commit()
        return '', 200


class CommentsData(Resource):
    def get(self, pid):
        post = Post.query.filter_by(pid=pid).first()
        comments = post.get_comments()
        comments_schema = CommentsSchema(many=True)
        data = comments_schema.dump(comments)
        return data

    def post(self, pid):
        content = request.json

        comment = Comment(
            content = content['content'],
            post_id = pid,
            user_id = content['user_id'],
        )
        db.session.add(comment)
        db.session.commit()    
        return 'Комментарий добавлен', 200
