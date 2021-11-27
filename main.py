import os
from flask import Flask
from flask import jsonify
from flask_migrate import Migrate

from api.config.config import SQLALCHEMY_DATABASE_URI, SQLALCHEMY_TRACK_MODIFICATIONS
from api.config.routes import generate_routes
# from api.database.create_test_data import create_test_data
from api.database.database import db


def create_app():
    app = Flask(__name__)
    app.config["DEBUG"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = SQLALCHEMY_TRACK_MODIFICATIONS

    # # YOLO
    # @app.route("/")
    # def wrapper_test():
    #     return jsonify(WRAPPER.search_movie_by_name("matrix"))

    generate_routes(app)

    # init Database
    db.init_app(app)

    # check if Database exists
    if not os.path.exists(SQLALCHEMY_DATABASE_URI):
        # create new if not exists
        db.app = app
        # create all tables
        db.create_all()

    # Fill some data for tests
    # create_test_data()
    migrate = Migrate(app, db)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(port=5000, debug=True, host="127.0.0.1", use_reloader=True)
