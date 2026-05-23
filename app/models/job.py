from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime

class Job(SQLModel, table=True):

    id: Optional[int] = Field(default=None, primary_key=True)

    type: str
    status: str = "PENDING"

    progress: int = 0

    error_message: Optional[str] = None

    started_at: datetime = Field(default_factory=datetime.utcnow)

    completed_at: Optional[datetime] = None