from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.domain.schemas.product import ProductCreate, ProductResponse
from app.services import product_service
from app.api.deps import get_db

router = APIRouter(prefix="/products", tags=["products"])


@router.post("/", response_model=ProductResponse)
def create(product: ProductCreate, db: Session = Depends(get_db)):
    return product_service.create_product_service(db, product)


@router.get("/{product_id}", response_model=ProductResponse)
def get(product_id: int, db: Session = Depends(get_db)):
    product = product_service.get_product_service(db, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return product


@router.get("/", response_model=list[ProductResponse])
def list_all(db: Session = Depends(get_db)):
    return product_service.list_products_service(db)
