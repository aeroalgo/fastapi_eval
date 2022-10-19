import asyncio
from fastapi.responses import JSONResponse
from fastapi import APIRouter, Response, Depends, HTTPException, status
from app.backend.src.core.logger.logg import logger
from concurrent.futures import ProcessPoolExecutor
from app.backend.src.eval.models.validation import Example, ResponseExample
from app.backend.src.eval.services.calculate_expression import Calculate

router = APIRouter()


@router.get("/")
async def hello():
    return Response('Hello world')


@router.get("/eval")
async def get_phrase(phrase: Example = Depends(), status_code=status.HTTP_200_OK, response_model=ResponseExample):
    """Метод принимает математическое выражение в виде строки query string"""
    if isinstance(phrase.phrase, HTTPException):
        return Response(status_code=400, content='Incorrect expression')
    loop = asyncio.get_event_loop()
    with ProcessPoolExecutor(max_workers=1) as executor:
        expression = await loop.run_in_executor(executor, Calculate, phrase.phrase)
    response_model = response_model(result=f'{phrase.phrase}={expression.result}')
    return Response(status_code=status_code, content=response_model.result)


@router.post("/eval")
async def post_phrase(phrase: Example, status_code=status.HTTP_201_CREATED, response_model=ResponseExample):
    """Метод принимает математическое выражение в json"""
    if isinstance(phrase.phrase, HTTPException):
        raise phrase.phrase
    loop = asyncio.get_event_loop()
    with ProcessPoolExecutor(max_workers=1) as executor:
        expression = await loop.run_in_executor(executor, Calculate, phrase.phrase)
    response_model = response_model(result=f'{phrase.phrase}={expression.result}')
    return JSONResponse(status_code=status_code, content=dict(response_model))
