import pandas as pd

from app.models.product import Product
from app.models.issue import Issue

from app.validators.product_validator import validate_product


def safe_str(value):

    if pd.isna(value):
        return ""

    return str(value)


def safe_float(value):

    if pd.isna(value):
        return 0.0

    try:
        return float(value)

    except (ValueError, TypeError):
        return 0.0


def process_csv_upload(file, session):

    df = pd.read_csv(file)

    created_products = 0

    for _, row in df.iterrows():

        product = Product(
            sku_id=safe_str(row.get("sku_id")),
            title=safe_str(row.get("product_title")),

            description=safe_str(row.get("description")),
            brand=safe_str(row.get("brand")),
            category=safe_str(row.get("category")),

            price=safe_float(row.get("price")),
            mrp=safe_float(row.get("mrp")),

            availability=safe_str(row.get("availability")),

            color=safe_str(row.get("color")),
            size=safe_str(row.get("size")),
            material=safe_str(row.get("material"))
        )

        session.add(product)
        session.commit()
        session.refresh(product)

        # safety check for pyright
        if product.id is None:
            continue

        issues = validate_product(product)

        for issue in issues:

            db_issue = Issue(
                product_id=product.id,
                severity=issue["severity"],
                message=issue["message"],
                suggested_fix=issue["suggested_fix"]
            )

            session.add(db_issue)

        created_products += 1

    session.commit()

    return {
        "message": "CSV processed successfully",
        "products_created": created_products
    }