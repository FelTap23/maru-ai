from fastapi import APIRouter
from choya.model.suma import SumaResponse, SumaRequest

router = APIRouter()

@router.post("/math", response_model=SumaResponse)
def suma( body : SumaRequest ):
    res = body.a + body.b 
    return SumaResponse(result=res)
    
@router.get("/math_param/{a}/{b}", response_model=SumaResponse)
def suma_path_param(a :int, b: int ):
    res = a + b
    return SumaResponse(result=res)

@router.get("/math_query", response_model=SumaResponse)
def suma_query_param(a :int, b: int ):
    res = a + b
    return SumaResponse(result=res)