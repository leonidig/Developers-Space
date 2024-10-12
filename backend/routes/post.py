from main import app
from db import (Session,
                Post)
from schemas import UserPostData


@app.post("/create_user_post")
def create_user_post(data: UserPostData):
    with Session.begin() as session:
        post = Post(**data.model_dump())
        session.add(post)
        return post