from fastapi import APIRouter

router = APIRouter()

@router.get("/amc")
def amc():
    return {
        "module": "AMC Module",
        "status": "working"
    }