from fastapi import APIRouter, Depends
import requests
from app.core.config import settings
from app.core.websocket import start_finnhub_websocket

router = APIRouter()

@router.get("/market-status")
async def market_news():
    """
    API to get latest market news.
    """
    params = {
        "token": settings.FINNHUB_API_KEY,
        "exchange": "US"
    }

    response = requests.get("https://finnhub.io/api/v1/market-status", params=params)
    return response.json()