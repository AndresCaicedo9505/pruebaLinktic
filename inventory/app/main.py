from fastapi import FastAPI
from app.api.routes import inventory

app = FastAPI(title="Microservicio de Inventario")
app.include_router(inventory.router)
