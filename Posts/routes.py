from flask import Blueprint

app = Blueprint("posts", __name__)


@app.route('/')
def index():
    return 'Index page of the posts module'
