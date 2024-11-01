from os import getenv

from flask_login import (current_user,
                         login_required)
from flask import (render_template,
                   request,
                   redirect,
                   url_for)
from requests import delete

from .. import app
from .request import APIClient


BACKEND_URL = getenv("BACKEND_URL")

client = APIClient(BACKEND_URL)


def to_index():
    return redirect(url_for("index"))


@app.get("/delete/<int:post_id>")
@login_required
def delete_validation(post_id):
    return render_template("delete.html", post_id=post_id)


@app.post("/delete/<int:post_id>")
@login_required  
def delete_post(post_id):
    choice = request.form.get("choice")
    if choice == "yes":
        data = {
            "post_id": post_id,
            "user": current_user.email
        }
        response = client.send_request(delete, f"/delete_user_post/{post_id}", data=data)
        if response.status_code == 200:
            return to_index()
        else:
            return render_template("error.html", message=response.text)
    else:
        return to_index()
