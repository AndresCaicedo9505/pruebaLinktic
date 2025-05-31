from app.services.inventory_service import process_purchase

def test_process_purchase_no_inventory(monkeypatch, test_db):
    import httpx

    def mock_httpx_get(url, headers, timeout):
        class MockResponse:
            status_code = 200
            def json(self):
                return {"id": 888, "nombre": "Producto Mock", "precio": 1.0}
        return MockResponse()

    monkeypatch.setattr(httpx, "get", mock_httpx_get)

    result = process_purchase(test_db, product_id=888, quantity=1)
    assert "error" in result
    assert result["error"] == "Inventario insuficiente"


def test_process_purchase_missing_product(monkeypatch, test_db):
    from app.clients import product_client
    monkeypatch.setattr(product_client, "fetch_product", lambda pid: None)
    result = process_purchase(test_db, product_id=999, quantity=1)
    assert "error" in result
    assert result["error"] == "Producto no existe"
