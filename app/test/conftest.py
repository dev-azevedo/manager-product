import pytest
from app.db.connection import Session
from app.db.models import Category as CategoryModel
from app.db.models import Product as ProductModel


@pytest.fixture()
def db_session():
    try:
        session = Session()
        yield session
    finally:
        session.close()

@pytest.fixture()
def categories_on_db(db_session):
    categories = [
        CategoryModel(name="Roupa", slug="roupa"),
        CategoryModel(name="Carro", slug="carro"),
        CategoryModel(name="Itens de cozinha", slug="itens-de-cozinha"),
        CategoryModel(name="Decoracao", slug="decoracao")
    ]
    
    for category in categories:
        db_session.add(category)
    db_session.commit()
    
    for category in categories:
        db_session.refresh(category)
        
    yield categories
    
    for category in categories:
        db_session.delete(category)
    db_session.commit()


@pytest.fixture()
def product_on_db(db_session):
    category = CategoryModel(name="Roupa", slug="roupa")
    db_session.add(category)
    db_session.commit()
    
    
    product = ProductModel(
        name="Camisa Adidas", 
        slug="camisa-adidas", 
        price=100.99, 
        stock=20,
        category_id=category.id
    )
    
    db_session.add(product)
    db_session.commit()
    
    yield product
    
    db_session.delete(product)
    db_session.delete(category)
    db_session.commit()
    
    
@pytest.fixture()
def products_on_db(db_session):
    category = CategoryModel(name="Roupa", slug="roupa")
    db_session.add(category)
    db_session.commit()
    db_session.refresh(category)
    
    products = [
       ProductModel(name="Camisa Adidas", slug="camisa-adidas", price=100.99, stock=20, category_id=category.id),
       ProductModel(name="Camisa Nike", slug="camisa-nike", price=22.99, stock=10, category_id=category.id),
       ProductModel(name="Camisa Puma", slug="camisa-puma", price=15.99, stock=5, category_id=category.id),
       ProductModel(name="Camisa Vans", slug="camisa-vans", price=20.99, stock=8, category_id=category.id),
    ]
    
    for product in products:
        db_session.add(product)
    db_session.commit()
    
    for product in products:
        db_session.refresh(product)
        
    yield products
    
    for product in products:
        db_session.delete(product)
        
    db_session.delete(category)
    db_session.commit()
