from datetime import datetime
from typing import Optional
from pydantic import BaseModel, ConfigDict


class UserPostData(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: Optional[int] = None
    author: str
    content: str
    theme: str
    published_at: datetime

class DeleteUserPost(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    user: str
    post_id: int

    