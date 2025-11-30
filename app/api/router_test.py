from fastapi import APIRouter
from app.services.google_sheet import read_test_sheet

router = APIRouter(prefix="/api")

@router.get("/test-read")
def test_read():
    data = read_test_sheet()
    return {"status": "ok", "rows": data}
