import httpx
from app.clients import product_client

def test_fetch_product_timeout(monkeypatch):
    def mock_get(*args, **kwargs):
        raise httpx.RequestError("timeout")
    monkeypatch.setattr(httpx, "get", mock_get)

    result = product_client.fetch_product(1)
    assert result is None