from os import getenv
from flask_login import (login_required,
                         current_user)
from flask import (render_template)
from requests import get
from .. import app


BACKEND_URL = getenv("BACKEND_URL")


@app.get("/user_post_info/<int:post_id>")
def user_post_info(post_id):
    response = get(f"{BACKEND_URL}/user_post_info/{post_id}")
    if response.status_code == 200:
        post = response.json()
        return render_template("info.html", post=post, post_id=post_id)
    else:
        return f"error: {response.status_code}"
