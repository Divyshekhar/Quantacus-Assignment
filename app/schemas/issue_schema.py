from pydantic import BaseModel

class IssueResponse(BaseModel):

    id: int
    product_id: int

    severity: str
    message: str
    suggested_fix: str