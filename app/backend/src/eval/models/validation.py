import re
from typing import *
from fastapi import HTTPException
from pydantic import BaseModel, Field, validator


class Example(BaseModel):
    phrase: str

    @validator("phrase")
    def check_phrase(cls, v):
        v = v.replace(' ', '+')
        if '"' in v:
            v = v.replace('"', '')
        elif "'" in v:
            v = v.replace("'", '')
        regExs = (r"^(?:\d+|\(\d+\s*[-+/*]\s*\d+\))(?:\s*[-+/*]\s*(?:\d+|\(\d+\s*[-+/*]\s*\d+\)))*$",)
        if not re.search(regExs[0], v):
            print(v)
            return HTTPException(status_code=400, detail="Incorrect expression")
        return v


class ResponseExample(BaseModel):
    result: str
