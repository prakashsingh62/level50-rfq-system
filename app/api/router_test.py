from fastapi import APIRouter
from datetime import datetime
from app.services.google_sheet import write_test_row

router = APIRouter(
    prefix="/test",
    tags=["Test API"]
)

@router.post("/write")
async def write_test_api():
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    values = ["TEST-WRITE", timestamp]
    result = write_test_row(values)
    return {
        "status": "OK",
        "written": True,
        "timestamp": timestamp,
        "result": result
    }
