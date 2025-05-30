from pydantic import BaseModel

class CompletionRequest(BaseModel):
    prompt : str

class CompletionResponse(BaseModel):
    output: str
