from sqlalchemy import Column, Integer, String, Float
from app.core.db import Base


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    precio = Column(Float, nullable=False)
    descripcion = Column(String, nullable=True)
