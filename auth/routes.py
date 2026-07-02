from fastapi import APIRouter

from auth.jwt_handler import create_access_token

router = APIRouter()

@router.post("/login")
async def login():
    token = create_access_token("user123")

    return {
        "access_token": token
    }