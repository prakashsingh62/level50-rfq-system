
from fastapi import FastAPI
from app.api.router_main import router as main_router
def register_routes(app:FastAPI):
    app.include_router(main_router)
