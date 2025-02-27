from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.providers.database import get_db
from app.schemas.schemas import ProductCreate, ProductResponse, ProductUpdate
from app.models.models import Product
from app.crud.crud import create_product, get_product

router = APIRouter(prefix="/products", tags=["products"])

@router.post("/", response_model=ProductResponse, status_code=status.HTTP_201_CREATED)
def create_new_product(product: ProductCreate, db: Session = Depends(get_db)):
    return create_product(db, product)

@router.get("/{id}", response_model=ProductResponse)
def read_product(id: int, db: Session = Depends(get_db)):
    product = get_product(db, id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@router.put("/{product_id}", response_model=ProductUpdate)
def update_product(product_id: int, product_update: ProductUpdate, db: Session = Depends(get_db)):
    product = db.query(Product).filter(Product.id == product_id).first()
    
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    product.name = product_update.name
    product.description = product_update.description

    db.commit()
    db.refresh(product)
    
    return product

@router.delete("/{product_id}", status_code=204)
def delete_product(product_id: int, db: Session = Depends(get_db)):
    product = db.query(Product).filter(Product.id == product_id).first()
    
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    db.delete(product)
    db.commit()
    
    return {"message": "Product deleted successfully"}
