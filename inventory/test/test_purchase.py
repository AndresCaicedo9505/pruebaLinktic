from app.clients import product_client

def test_purchase_success(monkeypatch, client):
    def mock_httpx_get(url, headers, timeout):
        class MockResponse:
            status_code = 200
            def json(self):
                return {"id": 201, "nombre": "Producto Mock", "precio": 10.0}
        return MockResponse()

    monkeypatch.setattr("httpx.get", mock_httpx_get)

    client.put("/inventory/201", json={"quantity": 5})
    response = client.post("/inventory/purchase", json={"product_id": 201, "quantity": 2})
    assert response.status_code == 200
    data = response.json()
    assert data["quantity_purchased"] == 2
    assert data["remaining_stock"] == 3

def test_purchase_insufficient_stock(monkeypatch, client):
    def mock_httpx_get(url, headers, timeout):
        class MockResponse:
            status_code = 200
            def json(self):
                return {"id": 202, "nombre": "Producto Mock", "precio": 10.0}
        return MockResponse()

    monkeypatch.setattr("httpx.get", mock_httpx_get)

    client.put("/inventory/202", json={"quantity": 1})
    response = client.post("/inventory/purchase", json={"product_id": 202, "quantity": 5})
    assert response.status_code == 400
    assert "Inventario insuficiente" in response.text

def test_purchase_invalid_product(monkeypatch, client):
    def mock_httpx_get(url, headers, timeout):
        class MockResponse:
            status_code = 404
            def json(self): return {}
        return MockResponse()

    monkeypatch.setattr("httpx.get", mock_httpx_get)

    response = client.post("/inventory/purchase", json={"product_id": 999, "quantity": 1})
    assert response.status_code == 400
    assert "Producto no existe" in response.text

