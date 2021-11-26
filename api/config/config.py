import os

basedir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# SQLALCHEMY_DATABASE_URI = "sqlite:///api/test.sqlite"
SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "manga.sqlite")
SQLALCHEMY_TRACK_MODIFICATIONS = False
