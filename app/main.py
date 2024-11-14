from fastapi import FastAPI
from app.routes.category_routes import router as category_routes
from app.routes.product_routes import router as product_routes
from app.routes.user_routes import router as user_routes

app = FastAPI()


@app.get("/health-check")
def read_root():
    return True

app.include_router(category_routes)
app.include_router(product_routes)
app.include_router(user_routes)