from fastapi import FastAPI

app = FastAPI()


@app.get("/weather")
async def weather():
    return [
          { 
            "state": 'AZ',
            "city": 'Mesa',
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