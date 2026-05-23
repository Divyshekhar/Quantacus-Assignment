from sqlmodel import SQLModel, Field
from typing import Optional

class Issue(SQLModel, table=True):

    id: Optional[int] = Field(default=None, primary_key=True)

    product_id: int

    severity: str
    message: str
    suggested_fix: str