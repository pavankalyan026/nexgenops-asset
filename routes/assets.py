from fastapi import APIRouter

router = APIRouter()

@router.get("/assets")
def assets():
    return {
        "module": "NexgenOps Asset",
        "status": "working"
    }