from pydantic import BaseModel

class SumaRequest(BaseModel):
    a : int
    b : int

class SumaResponse(BaseModel):
    result : int