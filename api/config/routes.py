from flask_restful import Api

from api.handlers.handlers import (
    CommentsData,
    FinanceData,
    Index,
    Login,
    PostChangeDelete,
    PostCreate,
    PostData,
    PostsData,
    RecomendationsData,
    UserData,
)


def generate_routes(app):
    '''Создание маршрутов API.'''
    api = Api(app)
    api.add_resource(Index, "/")
    api.add_resource(UserData, "/api/v1/users/<string:username>/")
    api.add_resource(PostData, "/api/v1/posts/<string:username>/")
    api.add_resource(PostsData, "/api/v1/followed/posts/<string:username>/")
    api.add_resource(
        RecomendationsData,
        "/api/v1/recomendations/<string:username>/"
    )
    api.add_resource(CommentsData, "/api/v1/comments/<int:id>/")
    api.add_resource(Login, "/api/v1/login")
    api.add_resource(FinanceData, "/api/v1/tickers/<string:username>/")
    api.add_resource(PostChangeDelete, "/api/v1/post/<int:pid>/")
    api.add_resource(PostCreate, "/api/v1/post/create/")
