from app.models.alert import Alert

def create_alert(
    session,
    product_id,
    severity,
    message
):

    alert = Alert(
        product_id=product_id,
        severity=severity,
        message=message
    )

    session.add(alert)
    session.commit()

    return alert