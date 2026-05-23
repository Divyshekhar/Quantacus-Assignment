from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime

class Alert(SQLModel, table=True):

    id: Optional[int] = Field(default=None, primary_key=True)

    product_id: int

    severity: str
    message: str

    created_at: datetime = Field(default_factory=datetime.utcnow)