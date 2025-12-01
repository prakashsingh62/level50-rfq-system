from fastapi import APIRouter
from app.services.write_engine_test import process_test_sheet

router = APIRouter(prefix="/test")

@router.post("/run-level50")
async def run_level50_test():
    result = process_test_sheet()
    return {
        "status": "OK",
        "mode": "TEST",
        "result": result
    }
