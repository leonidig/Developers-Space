from os import getenv
from flask_login import (current_user,
                         login_required)
from flask import (render_template,
                   request,
                   redirect,
                   url_for)
from requests import delete
from .. import app


BACKEND_URL = getenv("BACKEND_URL")


@app.get("/delete/<int:post_id>")
@login_required
def delete_validation(post_id):
    return render_template("delete.html", post_id=post_id)


@app.post("/delete/<int:post_id>")
def delete_post(post_id):
    response = request.form.get("choice")
    if response == "yes":
        data = {
            "post_id": post_id,
            "user": current_user.email
        }
        response = delete(f"{BACKEND_URL}/delete_user_post/{post_id}", json=data)
        if response.status_code == 200:
            return redirect(url_for("index"))
        else:
            # return render_template("errors.html", error_code=response.status_code, text=response.text)
    # else:
    #     return redirect(url_for("index"))