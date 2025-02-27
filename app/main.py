import os
from fastapi import FastAPI
from app.routers import products, orders

app = FastAPI(title="E-commerce API")


@app.get("/", tags=["Index"])
async def index():
    return {
        "message": f"{os.getenv("PROJECT_NAME")} is live on envionement {os.getenv("PROJECT_ENV")}"
    }


app.include_router(products.router)
app.include_router(orders.router)
