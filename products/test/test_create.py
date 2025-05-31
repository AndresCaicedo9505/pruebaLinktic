def test_create_product(client):
    response = client.post("/products/", json={
        "nombre": "Camiseta",
        "precio": 25.0,
        "descripcion": "Camiseta de algodón"
    })
    assert response.status_code == 200
    data = response.json()
    assert data["nombre"] == "Camiseta"
    assert data["precio"] == 25.0
    assert data["descripcion"] == "Camiseta de algodón"
    assert "id" in data
