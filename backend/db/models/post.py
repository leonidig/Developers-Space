from datetime import datetime
from sqlalchemy.orm import Mapped
from .. import Base


class Post(Base):
    __tablename__ = "posts"

    author: Mapped[str]
    content: Mapped[str]
    theme: Mapped[str]
    published_at: Mapped[datetime]