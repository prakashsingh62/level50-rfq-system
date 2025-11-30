from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.backend_api import register_routes

app = FastAPI(
    title="Level-50 RFQ System",
    version="50.0"
)

# Allow all origins (safe for your use)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register all backend routes (includes /api/test-read, /api/test-email, etc.)
register_routes(app)


@app.get("/")
def root():
    return {"status": "Level-50 RFQ Backend Running", "mode": "TEST", "version": "50.0"}


@app.get("/health")
def health():
    return {"ok": True, "version": "50.0"}
