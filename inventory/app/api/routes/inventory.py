from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.api.deps import get_db
from app.services.inventory_service import process_purchase
from app.repository.inventory_repository import get_inventory, update_inventory
from app.domain.schemas.inventory import InventoryUpdate, InventoryResponse, PurchaseRequest, PurchaseResponse

router = APIRouter(prefix="/inventory", tags=["inventory"])

@router.get("/{product_id}", response_model=InventoryResponse)
def read_inventory(product_id: int, db: Session = Depends(get_db)):
    item = get_inventory(db, product_id)
    if not item:
        raise HTTPException(status_code=404, detail="Producto no registrado en inventario")
    return item

@router.put("/{product_id}", response_model=InventoryResponse)
def update(product_id: int, payload: InventoryUpdate, db: Session = Depends(get_db)):
    return update_inventory(db, product_id, payload.quantity)

@router.post("/purchase", response_model=PurchaseResponse)
def purchase(payload: PurchaseRequest, db: Session = Depends(get_db)):
    result = process_purchase(db, payload.product_id, payload.quantity)
    if "error" in result:
        raise HTTPException(status_code=400, detail=result["error"])
    return result
