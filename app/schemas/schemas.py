from pydantic import BaseModel
from datetime import datetime
from typing import List

# Product Schemas
class ProductCreate(BaseModel):
    name: str
    description: str
    price: float

class ProductResponse(ProductCreate):
    id: int

    class Config:
        from_attributes = True

class ProductUpdate(BaseModel):
    name: str
    description: str


# Order Schemas
class OrderCreate(BaseModel):
    customer_id: int
    product_ids: List[int]

class OrderResponse(BaseModel):
    id: int
    customer_id: int
    status: str
    created_at: datetime

    class Config:
        from_attributes = True

class OrderStatusUpdate(BaseModel):
    status: str
