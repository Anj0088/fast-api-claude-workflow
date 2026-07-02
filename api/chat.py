from fastapi import APIRouter, Request

from middleware.limiter import limiter
from schema.chat import ChatRequest
from agents.orchestrator import execute

router = APIRouter()


@router.post("/chat")
@limiter.limit("20/minute")
async def chat(
    request: Request,
    chat_request: ChatRequest
):

    response = await execute(
        chat_request.message
    )

    return {
        "response": response
    }
