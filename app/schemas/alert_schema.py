from pydantic import BaseModel

class AlertResponse(BaseModel):

    id: int
    product_id: int

    severity: str
    message: str