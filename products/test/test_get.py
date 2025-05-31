def test_get_product(client):
    create = client.post("/products/", json={
        "nombre": "Zapato",
        "precio": 80.0,
        "descripcion": "Zapato deportivo"
    })
    pid = create.json()["id"]

    get = client.get(f"/products/{pid}")
    assert get.status_code == 200
    data = get.json()
    assert data["id"] == pid
    assert data["nombre"] == "Zapato"
