from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.ext.asyncio import AsyncSession
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.future import select

from .. import Base


class User(Base):
    __tablename__ = "users"

    email: Mapped[str]
    nickname: Mapped[str]
    password: Mapped[str]


    def set_password(self, password: str):
        self.password = generate_password_hash(password)

    def check_password(self, password: str) -> bool:
        return check_password_hash(self.password, password)
