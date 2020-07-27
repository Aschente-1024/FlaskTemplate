# Imports
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Database
db = SQLAlchemy()

from .models import *


def create_app():
    # instantiate the app
    app = Flask(__name__)
    app.config.from_object('CustomApi.config.BaseConfig')

    db.init_app(app)

    # enable CORS for unrestrected js request

    from .Posts.routes import app as posts
    from .Users.routes import app as users

    app.register_blueprint(posts)
    app.register_blueprint(users)

    return app
