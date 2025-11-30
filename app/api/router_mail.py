from fastapi import APIRouter

router = APIRouter(prefix="/mail")

@router.get("/unread")
def unread():
    return []

@router.get("/all")
def all_mails():
    return []

@router.get("/preview")
def preview():
    return []

router_send = APIRouter(prefix="/mail-send")

@router_send.post("/")
def mail_send():
    return {"sent":0}
