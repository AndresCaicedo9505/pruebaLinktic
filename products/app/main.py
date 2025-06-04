from fastapi import FastAPI
from app.api.routers import product

app = FastAPI(title="Microservicio de Productos")
app.include_router(product.router)
