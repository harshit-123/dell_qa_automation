from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.providers.database import get_db
from app.schemas.schemas import OrderCreate, OrderResponse, OrderStatusUpdate
from app.crud.crud import create_order, get_order
from app.models.models import Order
from datetime import datetime
from app.models.models import Product
router = APIRouter(prefix="/orders", tags=["orders"])

@router.post("/", response_model=OrderResponse, status_code=status.HTTP_201_CREATED)
def create_order(order_data: OrderCreate, db: Session = Depends(get_db)):
    # Validate that all products exist
    products = db.query(Product).filter(Product.id.in_(order_data.product_ids)).all()
    
    if len(products) != len(order_data.product_ids):
        raise HTTPException(status_code=400, detail="One or more products not found")

    # Create order
    new_order = Order(
        customer_id=order_data.customer_id,
        status="pending",
        created_at=datetime.utcnow()
    )
    
    db.add(new_order)
    db.commit()
    db.refresh(new_order)

    return new_order

@router.get("/{id}", response_model=OrderResponse)
def read_order(id: int, db: Session = Depends(get_db)):
    order = get_order(db, id)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return order

@router.put("/{order_id}/status", response_model=OrderStatusUpdate)
def update_order_status(order_id: int, order_update: OrderStatusUpdate, db: Session = Depends(get_db)):
    order = db.query(Order).filter(Order.id == order_id).first()
    
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")

    order.status = order_update.status
    db.commit()
    db.refresh(order)
    
    return order

@router.delete("/{order_id}", status_code=204)
def delete_order(order_id: int, db: Session = Depends(get_db)):
    order = db.query(Order).filter(Order.id == order_id).first()
    
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")

    db.delete(order)
    db.commit()
    
    return {"message": "Order deleted successfully"}
