from logging.config import dictConfig
from fastapi import FastAPI, Depends, HTTPException, Query
from fastapi.logger import logger as fastapi_logger
from fastapi.middleware.cors import CORSMiddleware
from models import *
from typing import List
import os
from sqlmodel import Session, select
from weather import createCacheDir, getWeather
from typing import List, Union
import logging
from config import LogConfig


app = FastAPI()

dictConfig(LogConfig().dict())
log = logging.getLogger("snowbird_weather")


if "CLIENT_URL" in os.environ:
    origins = [os.environ["CLIENT_URL"]]
else:
    # Local development URLs
    origins = [
        "http://localhost:8080",
    ]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

fastapi_logger.info(f"CORS origins: {origins}")

engine = create_db()


def get_session():
    with Session(engine) as session:
        yield session


createCacheDir()


@app.post(
    "/city_weather/", response_model=CityWithWeather, response_model_exclude_none=True
)
def city_weather(*, session: Session = Depends(get_session), city: CityBase):
    return getWeather(session, city)
