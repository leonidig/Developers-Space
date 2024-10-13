from typing import Any, Dict
from typing_extensions import Annotated, Doc
from fastapi import HTTPException


class PermissionDeniedForDeleteUserPost(HTTPException):
    def __init__(self, detail: str = "Permission Denied - Try Visit Another Page"):
        super().__init__(status_code=400, detail=detail)


class UserPostNotFound(HTTPException):
    def __init__(self, detail: str = "This Post Not Found"):
        super().__init__(status_code=404, detail=detail)


class ConectionWithDataBaseError(HTTPException):
    def __init__(self, status_code: int, detail: str = "Error runtime connection with database") -> None:
        super().__init__(status_code=503, detail=detail)