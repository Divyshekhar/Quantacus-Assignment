from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime

class CompetitorPrice(SQLModel, table=True):

    id: Optional[int] = Field(default=None, primary_key=True)

    product_id: int

    platform: str
    competitor_price: float

    competitor_url: Optional[str] = None

    last_checked_at: datetime = Field(default_factory=datetime.utcnow)