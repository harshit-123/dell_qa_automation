import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.providers.database import SessionLocal

client = TestClient(app)

# Dependency override for a clean database state in tests
@pytest.fixture(scope="function")
def db():
    db = SessionLocal()
    yield db
    db.close()

# Test: Create a Product
def test_create_product():
    response = client.post("/products/", json={
        "name": "Nike Shoes",
        "description": "Comfortable running shoes",
        "price": 1399.0
    })
    assert response.status_code == 201
    assert response.json()["name"] == "Nike Shoes"

# Test: Get a Product by ID
def test_get_product():
    response = client.get("/products/2")
    assert response.status_code == 200
    assert response.json()["name"] == "Samsung Galaxy S25 Ultra"

# Test: Update a Product's Name & Description
def test_update_product():
    response = client.put("/products/2", json={
        "name": "Updated Nike Shoes",
        "description": "Now with better cushioning!"
    })
    assert response.status_code == 200
    assert response.json()["name"] == "Updated Nike Shoes"

# Test: Delete a Product by ID
def test_delete_product():
    response = client.delete("/products/3")
    assert response.status_code == 204

# Test: Create an Order with Customer ID & Products
def test_create_order():
    response = client.post("/orders/", json={
        "customer_id": 2,
        "product_ids": [5, 6]
    })
    assert response.status_code == 201
    assert response.json()["customer_id"] == 2

# Test: Get an Order by ID
def test_get_order():
    response = client.get("/orders/2")
    assert response.status_code == 200

# Test: Update an Order's Status
def test_update_order_status():
    response = client.put("/orders/1/status", json={"status": "shipped"})
    assert response.status_code == 200
    assert response.json()["status"] == "shipped"

# Test: Delete an Order by ID
def test_delete_order():
    response = client.delete("/orders/2")
    assert response.status_code == 204

# Edge Case: Creating a Product with Missing Fields
def test_create_product_invalid():
    response = client.post("/products/", json={
        "name": "",
        "description": "",
        "price": -100
    })
    assert response.status_code == 422  # Validation error

# Edge Case: Fetching a Non-Existent Product
def test_get_non_existent_product():
    response = client.get("/products/999")
    assert response.status_code == 404
