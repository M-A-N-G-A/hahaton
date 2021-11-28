import logging
from datetime import datetime
from flask import g, request, jsonify
from flask_restful import Resource
from api.yahoo.finance import Stock
from pprint import pprint

import api.errors.errors as error



from api.database.database import db
from api.models.models import Comment, User, Post
from api.schemas.schemas import UserSchema, PostSchema, RecomendationsSchema, CommentsSchema


class Login(Resource):
    def post(self):
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
        user = User.query.filter_by(username=username).first()
        # create user schema for serializing
        user_schema = UserSchema()
        # get json data
        data = user_schema.dump(user)
        # return json from db
        return jsonify(data)


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


class PostsData(Resource):
    def get(self, username):
        user = User.query.filter_by(username=username).first()
        followed_posts = user.get_followed_posts()
        # create user schema for serializing
        post_schema = PostSchema(many=True)
        # get json data
        data = post_schema.dump(followed_posts)
        print(type(jsonify(data)))
        # return json from db
        return jsonify(data)


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
    def get(self, id):
        post = Post.query.filter_by(pid=id).first()
        comments = post.get_comments()
        comments_schema = CommentsSchema(many=True)
        data = comments_schema.dump(comments)
        return data

    def post(self, id):
        content = request.json

        comment = Comment(
            content = content['content'],
            post_id = id,
            user_id = content['user_id'],
        )
        db.session.add(comment)
        db.session.commit()    
        return 'Комментарий добавлен', 200

    def delete(self, id):
        comment_to_delete = Comment.query.filter_by(cid=id).first()
        if comment_to_delete:
            db.session.delete(comment_to_delete)
            db.session.commit()
            return 'Комментарий удален', 200
        return 'Такого комментария не существует', 409
    
    def put(self, id):
        comment_to_update = Comment.query.filter_by(cid=id).first()
        content = request.json

        if comment_to_update:
            comment_to_update.content = content['content']
            db.session.add(comment_to_update)
            db.session.commit()
            return 'Комментарий изменен', 200
        return 'Такого комментария не существует', 409

class FinanceData(Resource):
    def get(self, username):
        user = User.query.filter_by(username=username).first()
        ticker_list = user.stocks.strip().split()
        data = []
        for ticker in ticker_list:
            stock = Stock(ticker)
            price = stock.get_current_price()
            price_change = stock.get_price_change_percent()
            logo = stock.get_stock_logo()
            summary = stock.get_key_stats()
            summary = summary['longBusinessSummary']
            ticker_dict = {
                'ticker': ticker,
                'price': price,
                'price_change': round(price_change, 2),
                'logo': logo,
                'summary': summary,
            }
            data.append(ticker_dict)
        return jsonify(data)


class PostChangeDelete(Resource):
    def delete(self, pid):
            post_to_delete = Post.query.filter_by(pid=pid).first()
            if post_to_delete:
                db.session.delete(post_to_delete)
                db.session.commit()
                return 'Пост удален', 200
            return 'Такого поста не существует', 409
        
    def put(self, pid):
            post_to_update = Post.query.filter_by(pid=pid).first()
            content = request.json

            if post_to_update:
                post_to_update.content = content['content']
                db.session.add(post_to_update)
                db.session.commit()
                return 'Пост изменен', 200
            return 'Такого поста не существует', 409


class PostCreate(Resource):
    def post(self):
        post = Post(
            content = request.json['content'],
            user_id = request.json['user_id'],
            media = request.json['media'],
        )
        db.session.add(post)
        db.session.commit()
        return '', 200
