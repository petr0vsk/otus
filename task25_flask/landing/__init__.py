import os
from flask import Flask
from flask_wtf.csrf import CSRFProtect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
csrf = CSRFProtect(app)


db_path = os.path.join(os.path.dirname(__file__), 'db.sqlite3')
db_uri = 'sqlite:///{}'.format(db_path)

app.config.update(dict(
    SECRET_KEY="4b332#@@1!74-006b-4889-8#@#-67b#@#b90ddffd",
    WTF_CSRF_SECRET_KEY='8207bece0139#4980!af20a681e3bf56f3',
    SQLALCHEMY_DATABASE_URI=db_uri,
    SQLALCHEMY_TRACK_MODIFICATIONS=False,
))

db = SQLAlchemy(app)
db.init_app(app)
migrate = Migrate(app,db)
db.create_all()

from .home.views import *
from landing import db


