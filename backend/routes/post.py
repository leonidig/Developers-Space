"""All actions with user posts - CRUD, filters , etcetera"""

from sqlalchemy import select

from main import app
from db import (Session,
                Post
)
from schemas import (UserPostData,
                     DeleteUserPost
)
from exceptions import (PermissionDeniedForDeleteUserPost,
                        UserPostNotFound,
                        ConectionWithDataBaseError
)



@app.get("/")
def index():
    return {"Hello": "World!"}


@app.post("/create_user_post", status_code=201)
def create_user_post(data: UserPostData):
    """Create users post by schema UserPostData"""
    with Session.begin() as session:
        post = Post(**data.model_dump())
        session.add(post)
        return post


@app.get("/get_all_users_posts")
def get_all_users_posts():
    """Get all users posts"""
    try:
        with Session.begin() as session:
            posts = session.scalars(select(Post)).all()
            posts = [UserPostData.model_validate(post) for post in posts]
            return posts
    except Exception as e:
        raise ConectionWithDataBaseError()


@app.delete("/user_post/{post_id}")
def delete_user_post(data: DeleteUserPost):
    """Delete User Post"""
    with Session.begin() as session: 
        post_to_delete = session.scalar(select(Post).where(Post.id == data.post_id))
        if not post_to_delete:
            raise UserPostNotFound()
        elif post_to_delete.author != data.user:
            raise PermissionDeniedForDeleteUserPost()
        else:
            session.delete(post_to_delete)