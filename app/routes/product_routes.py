from fastapi import APIRouter, Depends
from sqlmodel import Session, select

from app.db.database import get_session

from app.models.product import Product
from app.models.issue import Issue

from app.services.title_enhancer_service import (
    generate_enhanced_title
)

router = APIRouter()

@router.get("/products")
def get_products(
    session: Session = Depends(get_session)
):

    return session.exec(
        select(Product)
    ).all()

@router.get("/products/{product_id}")
def get_product(
    product_id: int,
    session: Session = Depends(get_session)
):

    product = session.get(
        Product,
        product_id
    )

    return product

@router.get("/products/{product_id}/issues")
def get_product_issues(
    product_id: int,
    session: Session = Depends(get_session)
):

    issues = session.exec(
        select(Issue)
        .where(Issue.product_id == product_id)
    ).all()

    return issues

@router.post("/products/{product_id}/enhance-title")
def enhance_title(
    product_id: int,
    session: Session = Depends(get_session)
):

    product = session.get(
        Product,
        product_id
    )

    return generate_enhanced_title(product)