def test_update_inventory(client):
    response = client.put("/inventory/1", json={"quantity": 10})
    assert response.status_code == 200
    assert response.json()["quantity"] == 10

def test_read_inventory(client):
    response = client.get("/inventory/1")
    assert response.status_code == 200
    assert response.json()["product_id"] == 1

