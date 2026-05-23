from sqlmodel import select

from app.models.product import Product
from app.models.issue import Issue
from app.models.alert import Alert

def get_dashboard_metrics(session):

    products = session.exec(select(Product)).all()
    issues = session.exec(select(Issue)).all()
    alerts = session.exec(select(Alert)).all()

    high_issues = [
        issue for issue in issues
        if issue.severity == "HIGH"
    ]

    medium_issues = [
        issue for issue in issues
        if issue.severity == "MEDIUM"
    ]

    low_issues = [
        issue for issue in issues
        if issue.severity == "LOW"
    ]

    return {
        "total_products": len(products),
        "total_issues": len(issues),
        "high_issues": len(high_issues),
        "medium_issues": len(medium_issues),
        "low_issues": len(low_issues),
        "total_alerts": len(alerts)
    }