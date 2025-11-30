from fastapi import FastAPI
from app.backend_api import register_routes

app = FastAPI()
register_routes(app)
