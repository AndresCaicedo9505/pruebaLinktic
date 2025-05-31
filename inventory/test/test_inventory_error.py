def test_read_inventory_not_found(client):
    resp = client.get("/inventory/999")
    assert resp.status_code == 404
    assert "Producto no registrado" in resp.text

def test_update_inventory_then_read(client):
    resp = client.put("/inventory/55", json={"quantity": 10})
    assert resp.status_code == 200
    get_resp = client.get("/inventory/55")
    assert get_resp.status_code == 200
    assert get_resp.json()["quantity"] == 10
