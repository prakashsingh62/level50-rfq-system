from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.backend_api import register_routes

app = FastAPI(
    title="Level-50 RFQ System (TEST MODE)",
    version="50.0"
)

# CORS (required)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register ONLY test routes
register_routes(app)

@app.get("/")
def root():
    return {"status": "Level-50 TEST Backend Running", "version": "50.0"}

@app.get("/health")
def health():
    return {"ok": True, "mode": "TEST"}
