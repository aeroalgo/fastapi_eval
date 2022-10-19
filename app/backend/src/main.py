import uvicorn
from fastapi import FastAPI
from app.backend.src.core.logger.logg import logger
from app.backend.src.core.settings.conf import setting
from app.backend.src.eval.controllers.api import router as api


app = FastAPI()
app.include_router(api)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=setting.APP_PORT)
