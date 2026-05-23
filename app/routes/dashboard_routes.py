from fastapi import APIRouter, Depends
from sqlmodel import Session, select

from app.db.database import get_session

from app.models.product import Product
from app.models.issue import Issue
from app.models.alert import Alert

router = APIRouter()

@router.get("/dashboard/quality-summary")
def get_dashboard_summary(
    session: Session = Depends(get_session)
):

    products = session.exec(select(Product)).all()
    issues = session.exec(select(Issue)).all()
    alerts = session.exec(select(Alert)).all()

    return {
        "total_products": len(products),
        "total_issues": len(issues),
        "total_alerts": len(alerts)
    }