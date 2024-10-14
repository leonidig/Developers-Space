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


@app.delete("/delete_user_post/{post_id}")
def delete_user_post(data: DeleteUserPost):
    """Delete User Post"""
    try:
        with Session.begin() as session: 
            post_to_delete = session.scalar(select(Post).where(Post.id == data.post_id))
            if not post_to_delete:
                raise UserPostNotFound()
            elif post_to_delete.author != data.user:
                raise PermissionDeniedForDeleteUserPost()
            else:
                session.delete(post_to_delete)
    except Exception as e:
        raise ConectionWithDataBaseError()


@app.get("/user_post_info/{post_id}")
def user_post_info(post_id):
    try:
        with Session.begin() as session:
            selected_post = session.scalar(select(Post).where(Post.id == post_id))
            if selected_post is None:
                raise UserPostNotFound()
            else:
                selected_post = UserPostData.model_validate(selected_post)
                return selected_post
    except Exception as e:
        raise ConectionWithDataBaseError()


@app.get("/all_user_posts/{author}")
def all_user_posts(author: str):
    try: 
        with Session.begin() as session:
            all_user_posts = session.scalars(select(Post).where(Post.author == author)).all()
            all_user_posts = [UserPostData.model_validate(post) for post in all_user_posts]
            return all_user_posts
    except Exception as e:
        raise ConectionWithDataBaseError()