import httpx
from app.core.config import settings

def fetch_product(product_id: int):
    try:
        headers = {"X-API-KEY": settings.API_KEY}
        response = httpx.get(f"{settings.PRODUCTS_SERVICE_URL}/products/{product_id}", headers=headers, timeout=5)
        if response.status_code == 200:
            return response.json()
    except httpx.RequestError:
        return None
