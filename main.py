import os

from flask import Flask
from flask_migrate import Migrate

from api.config.config import (
    SQLALCHEMY_DATABASE_URI,
    SQLALCHEMY_TRACK_MODIFICATIONS as SQLTM,
)
from api.config.routes import generate_routes
from api.database.database import db


def create_app():
    '''Конфигурация приложения.'''
    app = Flask(__name__)
    app.config["DEBUG"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = SQLTM

    generate_routes(app)

    # Инициализация базы данных
    db.init_app(app)

    # Создание базы данных если её не существует
    if not os.path.exists(SQLALCHEMY_DATABASE_URI):
        db.app = app
        db.create_all()

    migrate = Migrate(app, db)
    return app


if __name__ == "__main__":
    # Создание приложения
    app = create_app()
    # Запуск приложения
    app.run(port=5000, debug=True, host="127.0.0.1", use_reloader=True)
