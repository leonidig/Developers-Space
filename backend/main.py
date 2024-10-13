"""Init FastAPI app"""
from fastapi import FastAPI


app = FastAPI(debug=True)


import routes
