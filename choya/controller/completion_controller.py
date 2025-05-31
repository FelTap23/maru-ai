from fastapi import APIRouter
from choya.model.completion import CompletionRequest,CompletionResponse


import logging
logger = logging.getLogger("maru_ai_main")
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')


router = APIRouter()


@router.get("/")
async def root():
    return {
        "message" : "Guoyootlot"
    }

@router.post("/completion", response_model=CompletionResponse)
async def completion(body : CompletionRequest):
    logger.info(f"Completion request received {body}")
    return  CompletionResponse(output="Hi How can I help you")