from fastapi import APIRouter
from choya.model.completion import CompletionRequest,CompletionResponse
from choya.service.completion_service import LlmService


import logging
logger = logging.getLogger("maru_ai_completion_controller")
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
    logger.info(f"Message recieved: {body}")
    llmservice = LlmService()
    response = llmservice.agent_chat(body)
    return  CompletionResponse(output=response)

