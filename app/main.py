from contextlib import asynccontextmanager
import logging

import dotenv


dotenv.load_dotenv()


import uvicorn
from fastapi import FastAPI

from app.routers import status, users
from app.database.engine import create_db_and_tables
from fastapi_pagination import add_pagination


@asynccontextmanager
async def lifespan(_: FastAPI):
    logging.warning("On startup")
    create_db_and_tables()
    yield
    logging.warning("On shutdown")

app = FastAPI(lifespan=lifespan)
app.include_router(status.router)
app.include_router(users.router)
add_pagination(app)


if __name__ == "__main__":
    uvicorn.run(app)