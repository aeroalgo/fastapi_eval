import asyncio
from fastapi.responses import ORJSONResponse
from concurrent.futures import ProcessPoolExecutor
from app.backend.src.core.logger.logg import logger
from fastapi import APIRouter, Response, Depends, HTTPException, status
from app.backend.src.eval.services.calculate_expression import Calculate
from app.backend.src.eval.models.validation import Example, ResponseExample

router = APIRouter()


@router.get("/")
async def hello():
    return Response('Hello world')


@router.get("/eval")
async def get_phrase(phrase: Example = Depends(Example), status_code=status.HTTP_200_OK):
    """Метод принимает математическое выражение в виде строки query string"""
    if isinstance(phrase.phrase, HTTPException):
        return Response(status_code=400, content='Incorrect expression')
    loop = asyncio.get_event_loop()
    with ProcessPoolExecutor(max_workers=1) as executor:
        expression = await loop.run_in_executor(executor, Calculate, phrase.phrase)
    example = ResponseExample(result=f'{phrase.phrase}={expression.result}')
    return Response(status_code=status_code, content=example.result)


@router.post("/eval", response_model=ResponseExample)
async def post_phrase(phrase: Example, status_code=status.HTTP_201_CREATED):
    """Метод принимает математическое выражение в json"""
    if isinstance(phrase.phrase, HTTPException):
        raise phrase.phrase
    loop = asyncio.get_event_loop()
    with ProcessPoolExecutor(max_workers=1) as executor:
        expression = await loop.run_in_executor(executor, Calculate, phrase.phrase)
    example = ResponseExample(result=f'{phrase.phrase}={expression.result}')
    return ORJSONResponse(status_code=status_code, content=dict(example))
