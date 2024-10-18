"""Init FastAPI app"""
from fastapi import FastAPI
from uvicorn import run as run_uvicorn



app = FastAPI(debug=True)


from . import routes


def main() -> None:
    run_uvicorn(app=app, port=8000)