from fastapi import APIRouter

router = APIRouter()

@router.post("/competitor-prices/refresh")
def refresh_prices():
    return {
        "message": "Competitor prices refreshed"
    }