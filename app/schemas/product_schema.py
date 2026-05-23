from pydantic import BaseModel
from typing import Optional

class ProductResponse(BaseModel):

    id: int
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