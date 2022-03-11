#!/usr/bin/env python3
import requests
import os
from bs4 import BeautifulSoup
from constants import STATE_ABV_TO_FULL, MONTHS
import random
import time
from models import CityBase, CityWithWeather
from sqlmodel import Session, select
import logging

WA_HTML_CACHE_DIR = os.path.join(os.path.dirname(__file__), "wa_html_cache")
CITIES_FILE = os.path.join(os.path.dirname(__file__), "cities.txt")
MONTHLY_WEATHER_CSV_FILE = os.path.join(os.path.dirname(__file__), "monthlyweather.csv")
FIRST_CALL_TO_RANDOM_DELAY = True
log = logging.getLogger("snowbird_weather")


def onHeroku():
    if "DYNO" in os.environ:
        return True


def random_delay(min_secs, max_secs):
    global FIRST_CALL_TO_RANDOM_DELAY
    if not FIRST_CALL_TO_RANDOM_DELAY:
        delay = random.randrange(min_secs, max_secs)
        log.info(f"Waiting {delay} seconds so we don't look like a bot...")
        time.sleep(delay)
    else:
        FIRST_CALL_TO_RANDOM_DELAY = False


def wa_scrape(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36",
        "Referer": "https://duckduckgo.com/",
    }
    log.info(f"Getting url: {url}...")
    random_delay(0, 5)
    req = requests.get(url, timeout=120, headers=headers, allow_redirects=False)
    req.raise_for_status()
    if req.status_code == 301:
        # We got redirected which means the city is invalid
        return None
    if req.status_code == 200:
        return req.text
    raise Exception(f"Unknown status code for {url}: {req}")


def createCacheDir():
    if onHeroku():
        log.info("On Heroku, don't bother caching files.")
        return
    if not os.path.exists(WA_HTML_CACHE_DIR):
        log.info(f"Creating {WA_HTML_CACHE_DIR} for caching html files.")
        os.mkdir(WA_HTML_CACHE_DIR)


def getCacheFile(city: CityBase):
    return os.path.join(
        WA_HTML_CACHE_DIR, f"{city.state.lower()}-{city.name.lower()}.html"
    )


# Use the casing from WA instead of user
def fixCityName(city: CityBase, soup: BeautifulSoup):
    city.name = soup.title.text.split(f", {city.state} ")[0]


def getWeather(session: Session, city: CityBase):
    # Using like to do a case insensitive search
    db_city = session.exec(
        select(CityWithWeather)
        .where(CityWithWeather.name.like(f"{city.name}"))
        .where(CityWithWeather.state == city.state)
    ).first()
    if not db_city:
        log.info(f"NO CACHE! {city.name}, {city.state} not found, creating it.")
        db_city = CityWithWeather.from_orm(city)
        addWeather(db_city)
        session.add(db_city)
        session.commit()
        session.refresh(db_city)  # Not sure if I need this
    else:
        log.info(f"FOUND IN CACHE! {city.name}, {city.state}.")
    log.info(f"Using db record {db_city}")
    return session.get(CityWithWeather, db_city.id)


def addWeather(city: CityWithWeather):
    html_doc = geHtmlFromWeatherAtlas(city)
    if not html_doc:
        return
    soup = BeautifulSoup(html_doc, "html.parser")
    if not soup:
        return
    for month in MONTHS:
        for high_low in ["high", "low"]:
            temp = (
                soup.find(
                    title=f"Climate data - {month}",
                    string=f"Average {high_low} temperature in {month}",
                )
                .findNext(name="span")
                .text
            )
            if not temp.endswith("°C"):
                raise Exception(
                    f"Could not extract temperature for {month} from {city}"
                )
            fahrenheit = round((float(temp[:-2]) * 1.8) + 32)
            setattr(city, f"{month.lower()}_{high_low}", fahrenheit)
    fixCityName(city, soup)


def geHtmlFromWeatherAtlas(city: CityBase) -> BeautifulSoup:
    cache_file = getCacheFile(city)
    if onHeroku() or not os.path.exists(cache_file):
        city_url_param = city.name.lower().replace(" ", "-").replace("'", "")
        state_url_param = STATE_ABV_TO_FULL[city.state].lower().replace(" ", "-")
        url = f"https://www.weather-atlas.com/en/{state_url_param}-usa/{city_url_param}-climate?f,in,in,mi"
        html_doc = wa_scrape(url)
        if not html_doc:
            return None
        if onHeroku():
            return html_doc
        log.info(f"Caching data to {cache_file}")
        with open(cache_file, "w") as save_fh:
            save_fh.write(html_doc)
    else:
        log.info(f"Using cache for  {city.name}, {city.state}.")
    with open(cache_file, "r") as cache_fh:
        html_doc = "\n".join(cache_fh.readlines())
    return html_doc
