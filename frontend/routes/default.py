from os import getenv
from requests import get
from flask import render_template
from flask_login import current_user, login_required
from .. import app
from .request import APIClient


BACKEND_URL = getenv("BACKEND_URL")


client = APIClient(BACKEND_URL)

@app.get("/")
@login_required
def index():
    email = current_user.email
    response = client.send_request(get, "/get_all_users_posts")
    posts = {
        "posts": response.json()
    }
    nickname = email.split("@")[0]
    return render_template("__base.html", **posts, nickname=nickname)
