from sqlalchemy.orm import Session
from app.repository import inventory_repository
from app.clients.product_client import fetch_product

def process_purchase(db: Session, product_id: int, quantity: int):
    product = fetch_product(product_id)
    if not product:
        return {"error": "Producto no existe"}
    item = inventory_repository.get_inventory(db, product_id)
    if not item or item.quantity < quantity:
        return {"error": "Inventario insuficiente"}
    updated = inventory_repository.reduce_inventory(db, product_id, quantity)
    return {
        "product_id": product_id,
        "quantity_purchased": quantity,
        "remaining_stock": updated.quantity,
    }
