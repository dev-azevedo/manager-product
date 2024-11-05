from fastapi import APIRouter, Response, Depends, status
from sqlalchemy.orm import Session
from app.routes.deps import get_db_session
from app.use_cases.product import ProductUseCase
from app.schemas.product import Product, ProductInput


router = APIRouter(prefix="/product")

@router.post("/add")
def add_product(product_input: ProductInput, db_session: Session = Depends(get_db_session)):
    uc = ProductUseCase(db_session)
    uc.add_product(product_input.product, product_input.category_slug)
    return Response(status_code=status.HTTP_201_CREATED)
