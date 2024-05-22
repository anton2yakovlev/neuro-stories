import uvicorn
from contextlib import asynccontextmanager
from fastapi import FastAPI
from api import router as api_router

from core.models.db_helper import db_helper
from core.config import settings


@asynccontextmanager
async def lifespan(app: FastAPI):
    # startup
    yield
    # shutdown
    await db_helper.dispose()


app = FastAPI(lifespan=lifespan)
app.include_router(api_router, prefix=settings.api.prefix)


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=settings.run.host,
        port=settings.run.port,
        reload=True,
    )
