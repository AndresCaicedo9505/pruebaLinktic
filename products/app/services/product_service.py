from sqlalchemy.orm import Session
from app.repository import product_repository
from app.domain.schemas.product import ProductCreate


def create_product_service(db: Session, product: ProductCreate):
    return product_repository.create_product(db, product)


def get_product_service(db: Session, product_id: int):
    return product_repository.get_product(db, product_id)


def list_products_service(db: Session):
    return product_repository.list_products(db)
