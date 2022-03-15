from logging.config import dictConfig
from fastapi import FastAPI, Depends, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from models import CityWithWeather, CityBase, create_db
from typing import List
import os
from sqlmodel import Session
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

log.info(f"CORS origins: {origins}")

engine = create_db()


def get_session():
    with Session(engine) as session:
        yield session


createCacheDir()


@app.post(
    "/city_weather/", response_model=CityWithWeather, response_model_exclude_none=True
)
def city_weather(*, session: Session = Depends(get_session), city: CityBase):
    log.info(f"Getting weather for {city}...")
    try:
        return getWeather(session, city)
    except Exception as e:
        log.error("Exception: " + e)


@app.post(
    "/cities_weather/",
    response_model=List[CityWithWeather],
    response_model_exclude_none=True,
)
def city_weather(*, session: Session = Depends(get_session), cities: List[CityBase]):
    cities_with_weather: List[CityWithWeather] = []
    for city in cities:
        cities_with_weather.append(getWeather(session, city))
    return cities_with_weather
