from pydantic import BaseModel
from typing import Optional

class JobResponse(BaseModel):

    id: int

    type: str
    status: str

    progress: int

    error_message: Optional[str] = None