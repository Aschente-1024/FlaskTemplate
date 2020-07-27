"""
    config.py
    - settings for the flask application object
"""


class ConfigClass(object):
    DEBUG = True
    SECRET_KEY = 'my secret key'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///my_test_db.sqlite'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    PRESERVE_CONTEXT_ON_EXCEPTION = False
