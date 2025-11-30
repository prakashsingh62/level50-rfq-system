from fastapi import APIRouter

router = APIRouter(prefix="/jobs")

@router.post("/run-daily")
def run_daily():
    return {"info":"daily job placeholder"}

@router.post("/run-full")
def run_full():
    return {"info":"full workflow placeholder"}
