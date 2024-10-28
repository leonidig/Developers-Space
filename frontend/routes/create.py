from os import getenv
from requests import post
from flask import (render_template,
                   request,
                   redirect,
                   url_for)
from flask_login import current_user, login_required
from .. import app
from .request import APIClient


BACKEND_URL = getenv("BACKEND_URL")


client = APIClient(BACKEND_URL)


@app.get("/create")
def create():
    return render_template("create.html")


@app.post("/create")
@login_required
def create_post():
    data = {
        "author": current_user.email,
        "content": request.form.get("content"),
        "theme": request.form.get("theme")
    }
    print("!" * 80)
    print(data)
    response = client.send_request(post, "/create_user_post", data=data)
    if response.status_code == 201:
        return redirect(url_for("index"))
    else:
        print("*" * 80)
        print(f"Code - {response.status_code}\nText - {response.text}")
        return redirect(url_for("index"))