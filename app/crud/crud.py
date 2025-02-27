from sqlalchemy.orm import Session
from starlette.status import HTTP_400_BAD_REQUEST
from fastapi import HTTPException
from app.models.models import Product, Order
from app.schemas.schemas import ProductCreate, OrderCreate

# CRUD for Products
def create_product(db: Session, product: ProductCreate):
    if product.name is "" or product.description is "":
        raise HTTPException(status_code=422, detail="Product not found")
    db_product = Product(**product.model_dump())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def get_product(db: Session, product_id: int):
    return db.query(Product).filter(Product.id == product_id).first()

# CRUD for Orders
def create_order(db: Session, order: OrderCreate):
    db_order = Order(customer_id=order.customer_id)
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order

def get_order(db: Session, order_id: int):
    return db.query(Order).filter(Order.id == order_id).first()
