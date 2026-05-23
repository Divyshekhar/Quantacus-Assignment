from fastapi import APIRouter, Depends
from sqlmodel import Session, select

from app.db.database import get_session
from app.models.alert import Alert

router = APIRouter()

@router.get("/alerts")
def get_alerts(
    session: Session = Depends(get_session)
):
    alerts = session.exec(select(Alert)).all()
    return alerts