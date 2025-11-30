
from fastapi import APIRouter
router = APIRouter()
@router.get("/")
def root():
    return {"status":"Level-50 RFQ Backend Running","mode":"TEST","version":"50.0"}
@router.get("/health")
def health():
    return {"ok":True,"version":"50.0"}
