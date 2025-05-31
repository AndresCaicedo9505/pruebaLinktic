from app.repository import inventory_repository
from app.domain.models.inventory import Inventory

def test_update_inventory_new_item(test_db):
    item = inventory_repository.update_inventory(test_db, product_id=10, quantity=7)
    assert item.product_id == 10
    assert item.quantity == 7

def test_update_inventory_existing_item(test_db):
    inventory_repository.update_inventory(test_db, product_id=20, quantity=5)
    updated = inventory_repository.update_inventory(test_db, product_id=20, quantity=12)
    assert updated.quantity == 12

def test_get_inventory_empty(test_db):
    item = inventory_repository.get_inventory(test_db, 9999)
    assert item is None

def test_reduce_inventory_success(test_db):
    inventory_repository.update_inventory(test_db, 30, 10)
    item = inventory_repository.reduce_inventory(test_db, 30, 4)
    assert item.quantity == 6

def test_reduce_inventory_fail(test_db):
    inventory_repository.update_inventory(test_db, 40, 2)
    result = inventory_repository.reduce_inventory(test_db, 40, 5)
    assert result is None