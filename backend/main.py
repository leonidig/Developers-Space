"""Init FastAPI app"""
from fastapi import FastAPI
from uvicorn import run as run_uvicorn


app = FastAPI(debug=True)


import routes


def main() -> None:
    run_uvicorn(app=app, host="0.0.0.0", port=8000)
