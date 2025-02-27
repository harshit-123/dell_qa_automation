# E-Commerce API

This is a FastAPI-based e-commerce API that allows users to manage products and orders with full CRUD operations, filtering, and sorting.

## Features
- ✅ CRUD operations for **Products** and **Orders**
- ✅ Filtering and sorting capabilities
- ✅ Uses **PostgreSQL** with **SQLAlchemy** and **Alembic** for database migrations
- ✅ API documentation available at `/docs` (Swagger UI)

## Technologies Used
- **Python 3.11+**
- **FastAPI** (for API development)
- **SQLAlchemy** (ORM for PostgreSQL)
- **Alembic** (Database migrations)
- **Pydantic** (Data validation)
- **Uvicorn** (ASGI server for running FastAPI)

---

## 🚀 Getting Started

### **1️⃣ Clone the Repository**
```sh
git clone https://github.com/yourusername/ecommerce-api.git
cd ecommerce-api
```

### **2️⃣ Create and Activate Virtual Environment**
```sh
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate    # On Windows
```

### **3️⃣ Install Dependencies**
```sh
pip install -r requirements.txt
```

### **4️⃣ Configure Database (PostgreSQL)**
1. Create a PostgreSQL database:
```sql
CREATE DATABASE ecommerce_db;
```
2. Update `app/config.py` with database credentials:
```python
DATABASE_URL = "postgresql://your_user:your_password@localhost/ecommerce_db"
```

### **5️⃣ Run Database Migrations**
```sh
alembic upgrade head
```

### **6️⃣ Start the API Server**
```sh
uvicorn main:app --reload
```

API will be available at: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 📌 API Endpoints

### **1️⃣ Product Endpoints**
| Method | Endpoint             | Description                  |
|--------|----------------------|------------------------------|
| `POST` | `/products/`         | Create a new product        |
| `GET`  | `/products/{id}`     | Get a product by ID         |
| `PUT`  | `/products/{id}`     | Update product name & desc  |
| `DELETE` | `/products/{id}`   | Delete a product by ID      |

#### **Create a Product**
```http
POST /products/
Content-Type: application/json
{
    "name": "Nike Shoes",
    "description": "Comfortable running shoes",
    "price": 1399.0
}
```

#### **Update a Product**
```http
PUT /products/1
{
    "name": "Updated Nike Shoes",
    "description": "Now with better cushioning!"
}
```

#### **Delete a Product**
```http
DELETE /products/1
```

---

### **2️⃣ Order Endpoints**
| Method | Endpoint               | Description                          |
|--------|------------------------|--------------------------------------|
| `POST` | `/orders/`             | Create an order                     |
| `GET`  | `/orders/{id}`         | Get an order by ID                   |
| `PUT`  | `/orders/{id}/status`  | Update order status (e.g., shipped)  |
| `DELETE` | `/orders/{id}`        | Delete an order by ID                |

#### **Create an Order**
```http
POST /orders/
Content-Type: application/json
{
    "customer_id": 1,
    "product_ids": [1, 2, 3]
}
```

#### **Update Order Status**
```http
PUT /orders/1/status
{
    "status": "shipped"
}
```

#### **Delete an Order**
```http
DELETE /orders/1
```

---

## 🔥 API Documentation
Once the server is running, visit:
- 📜 Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- 📜 Redoc UI: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## 🧪 Running Tests
1. Install `pytest`:
```sh
pip install pytest
```
2. Run tests:
```sh
pytest tests/
```

---

## 📜 License
This project is licensed under the MIT License.

---

## 🤝 Contributions
Contributions are welcome! Feel free to open an issue or submit a pull request. 😊

