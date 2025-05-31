from sqlalchemy import Column, Integer
from app.core.db import Base

class Inventory(Base):
    __tablename__ = "inventory"

    product_id = Column(Integer, primary_key=True, index=True)
    quantity = Column(Integer, nullable=False)
