from sqlalchemy.orm import Session
from app.domain.models.product import Product
from app.domain.schemas.product import ProductCreate


def create_product(db: Session, product_data: ProductCreate):
    product = Product(**product_data.dict())
    db.add(product)
    db.commit()
    db.refresh(product)
    return product


def get_product(db: Session, product_id: int):
    return db.query(Product).filter(Product.id == product_id).first()


def list_products(db: Session):
    return db.query(Product).all()
