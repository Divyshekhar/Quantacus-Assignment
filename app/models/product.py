from sqlmodel import SQLModel, Field
from typing import Optional

class Product(SQLModel, table=True):

    id: Optional[int] = Field(default=None, primary_key=True)

    sku_id: str
    title: str

    description: Optional[str] = None
    brand: Optional[str] = None
    category: Optional[str] = None

    price: float
    mrp: Optional[float] = None

    availability: Optional[str] = None

    color: Optional[str] = None
    size: Optional[str] = None
    material: Optional[str] = None

    quality_score: Optional[float] = 0