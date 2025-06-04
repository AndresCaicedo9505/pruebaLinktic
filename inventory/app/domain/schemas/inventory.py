from pydantic import BaseModel

class InventoryUpdate(BaseModel):
    quantity: int

class InventoryResponse(BaseModel):
    product_id: int
    quantity: int

    class Config:
        orm_mode = True

class PurchaseRequest(BaseModel):
    product_id: int
    quantity: int

class PurchaseResponse(BaseModel):
    product_id: int
    quantity_purchased: int
    remaining_stock: int
