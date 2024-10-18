import logging

from sqlalchemy import select

from ..db import (Session,
                  Post)
from ..exceptions import (PermissionDeniedForDeleteUserPost,
                          UserPostNotFound,
                          ConectionWithDataBaseError)
from ..schemas import (UserPostData,
                       DeleteUserPost)

from .. import app

logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger()


def handle_database_exception(func):
    """Wraper for handling error in database"""
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logger.error(f"Database error: {e}")
            raise
    return wrapper


@app.get("/")
def index():
    return {"Hello": "World!"}


@app.post("/create_user_post", status_code=201)
# @handle_database_exception
def create_user_post(data: UserPostData):
    """Create users post by schema UserPostData"""
    with Session.begin() as session:
        post = Post(**data.model_dump())
        session.add(post)
        return post


@app.get("/get_all_users_posts")
# @handle_database_exception
def get_all_users_posts():
    """Get all users posts"""
    with Session.begin() as session:
        posts = session.scalars(select(Post)).all()
        posts = [UserPostData.model_validate(post) for post in posts]
        return posts


@app.delete("/delete_user_post/{post_id}")
@handle_database_exception
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


@app.get("/user_post_info/{post_id}")
@handle_database_exception
def user_post_info(post_id: int):
    """Get user post information by post_id"""
    with Session.begin() as session:
        selected_post = session.scalar(select(Post).where(Post.id == post_id))
        if selected_post is None:
            raise UserPostNotFound()
        return UserPostData.model_validate(selected_post)


@app.get("/all_user_posts/{author}")
@handle_database_exception
def all_user_posts(author: str):
    """Get all posts by a specific author"""
    with Session.begin() as session:
        all_user_posts = session.scalars(select(Post).where(Post.author == author)).all()
        all_user_posts = [UserPostData.model_validate(post) for post in all_user_posts]
        return all_user_posts