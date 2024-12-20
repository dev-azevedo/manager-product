import pytest
from fastapi import HTTPException
from app.db.models import Product as ProductModel
from app.schemas.product import Product, ProductOutput
from app.use_cases.product import ProductUseCases


def test_add_product_uc(db_session, categories_on_db):
    uc = ProductUseCases(db_session)
    
    product = Product(name="Camisa Nike", slug="camisa-nike", price=22.99, stock=10)
    
    uc.add_product(product=product, category_slug=categories_on_db[0].slug)
    
    product_on_db = db_session.query(ProductModel).first()
    
    assert product_on_db is not None
    assert product_on_db.name == product.name
    assert product_on_db.slug == product.slug
    assert product_on_db.price == product.price
    assert product_on_db.stock == product.stock
    assert product_on_db.category.name == categories_on_db[0].name
    
    db_session.delete(product_on_db)
    db_session.commit()

def test_add_product_uc_invalid_category(db_session):
    uc = ProductUseCases(db_session)
    
    product = Product(name="Camisa Nike", slug="camisa-nike", price=22.99, stock=10)
    
    with pytest.raises(HTTPException):
        uc.add_product(product=product, category_slug='invalid-category')
    
def test_update_product_uc(db_session, product_on_db):
    product = Product(name="Camisa Nike", slug="camisa-nike", price=22.99, stock=10)
    
    uc = ProductUseCases(db_session=db_session)
    uc.update_product(id=product_on_db.id, product=product)
    
    product_update_on_db = db_session.query(ProductModel).filter_by(id=product_on_db.id).first()
    
    assert product_update_on_db is not None
    assert product_update_on_db.name == product.name
    assert product_update_on_db.slug == product.slug
    assert product_update_on_db.price == product.price
    assert product_update_on_db.stock == product.stock
    
def test_update_product_uc_invalid_id(db_session, product_on_db):
    product = Product(name="Camisa Nike", slug="camisa-nike", price=22.99, stock=10)
    
    uc = ProductUseCases(db_session=db_session)
    
    with pytest.raises(HTTPException):
        uc.update_product(id=0, product=product)
        
def test_delete_product_uc(db_session, product_on_db):
    uc = ProductUseCases(db_session=db_session)
    
    uc.delete_product(id=product_on_db.id)
    
    products_on_db = db_session.query(ProductModel).all()
    assert len(products_on_db) == 0
    
def test_delete_product_uc_invalid_id(db_session):
    uc = ProductUseCases(db_session=db_session)
    
    with pytest.raises(HTTPException):
        uc.delete_product(id=0)
        
def test_list_products_uc(db_session, products_on_db):
    uc = ProductUseCases(db_session=db_session)
    
    products = uc.list_products()
    
    for product in products_on_db:
        db_session.refresh(product)
    
    assert len(products) == 4
    assert type(products[0]) == ProductOutput
    assert products[0].name == products_on_db[0].name
    assert products[0].category.name == products_on_db[0].category.name
    
def test_list_products_with_search_uc(db_session, products_on_db):
    uc = ProductUseCases(db_session=db_session)
    
    products = uc.list_products(search='vans')
    
    for product in products_on_db:
        db_session.refresh(product)
    
    assert len(products) == 1
    assert type(products[0]) == ProductOutput
    
    