from app.api.router_test import router as test_router
from fastapi import FastAPI
from app.api.router_main import router as main_router
from app.api.router_rfq import router as rfq_router
from app.api.router_mail import router as mail_router
from app.api.router_jobs import router as jobs_router

def register_routes(app:FastAPI):
    app.include_router(main_router)
    app.include_router(rfq_router)
    app.include_router(mail_router)
    app.include_router(jobs_router)
    app.include_router(test_router)
