from flask import Blueprint

app = Blueprint("users", __name__)


@app.route('/')
def index():
    return 'Index page of the users module'
