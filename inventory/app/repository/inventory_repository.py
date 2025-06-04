from sqlalchemy.orm import Session
from app.domain.models.inventory import Inventory

def get_inventory(db: Session, product_id: int):
    return db.query(Inventory).filter(Inventory.product_id == product_id).first()

def update_inventory(db: Session, product_id: int, quantity: int):
    item = get_inventory(db, product_id)
    if item:
        item.quantity = quantity
    else:
        item = Inventory(product_id=product_id, quantity=quantity)
        db.add(item)
    db.commit()
    db.refresh(item)
    return item

def reduce_inventory(db: Session, product_id: int, quantity: int):
    item = get_inventory(db, product_id)
    if not item or item.quantity < quantity:
        return None
    item.quantity -= quantity
    db.commit()
    db.refresh(item)
    return item
