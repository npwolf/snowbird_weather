from typing import Optional
from pydantic import constr, validator
from datetime import datetime
from sqlmodel import (
    Field,
    SQLModel,
    create_engine,
    UniqueConstraint,
)
from time import sleep
from constants import STATE_ABV_TO_FULL
import os
import logging

log = logging.getLogger("snowbird_weather")


class CityBase(SQLModel):
    __table_args__ = (UniqueConstraint("name", "state"),)
    name: constr(max_length=40, min_length=3, strip_whitespace=True)
    state: constr(max_length=2, min_length=2, strip_whitespace=True)

    @validator("state")
    def valid_state(cls, v):
        v = v.upper()
        if v not in STATE_ABV_TO_FULL:
            raise ValueError(f"{v} is not a valid state.")
        return v


class CityWithWeather(CityBase, table=True):
    id: Optional[int] = Field(
        default=None,
        primary_key=True,
    )
    created_at: datetime = Field(default=datetime.utcnow(), nullable=False)
    january_high: Optional[int]
    january_low: Optional[int]
    february_high: Optional[int]
    february_low: Optional[int]
    march_high: Optional[int]
    march_low: Optional[int]
    april_high: Optional[int]
    april_low: Optional[int]
    may_high: Optional[int]
    may_low: Optional[int]
    june_high: Optional[int]
    june_low: Optional[int]
    july_high: Optional[int]
    july_low: Optional[int]
    august_high: Optional[int]
    august_low: Optional[int]
    september_high: Optional[int]
    september_low: Optional[int]
    october_high: Optional[int]
    october_low: Optional[int]
    november_high: Optional[int]
    november_low: Optional[int]
    december_high: Optional[int]
    december_low: Optional[int]


def create_db():

    if os.getenv("DATABASE_URL"):
        # Heroku
        database_url = os.environ["DATABASE_URL"]
        # SQLAlchemy doesn't allow the old prefix (for heroku)
        database_url = database_url.replace("postgres://", "postgresql://")
    else:
        sqlite_file_name = "database.db"
        if os.path.exists(sqlite_file_name):
            log.info("Using existing file database!")
        database_url = f"sqlite:///{sqlite_file_name}"
    log.info(f"Database URL: {database_url}")
    engine = create_engine(database_url, echo=True)
    SQLModel.metadata.create_all(engine, checkfirst=True)
    return engine
