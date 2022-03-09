from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI()

origins = [
    "http://localhost:8080",
]

if "CLIENT_URL" in os.environ:
    origins.append(os.environ["CLIENT_URL"])

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/weather")
async def weather():
    return [
          { 
            "state": 'AZ',
            "city": 'Phoenix',
            "january": { 
                "high": 60, 
                "low": 45
                },
          },
          {
            "state": 'MT',
            "city": 'Bozeman',
            "january": { 
                "high": 45, 
                "low": 20
                },
          },]