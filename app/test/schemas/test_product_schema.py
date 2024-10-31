import pytest
from app.schemas.product import Product

def test_product_schema():
    product = Product(
        name="Camisa Nike",
        slug="camisa-nike",
        price=22.99,
        stock=10
    )
    
    assert product.name == "Camisa Nike"
    assert product.slug == "camisa-nike"
    assert product.price == 22.99
    assert product.stock == 10
    
    
def test_product_schema_invalid_slug():
    with pytest.raises(ValueError):
        product = Product(
            name="Camisa Nike",
            slug="camisa nike",
            price=22.99,
            stock=10
        )
        
    with pytest.raises(ValueError):
        product = Product(
            name="Camisa Nike",
            slug="cão",
            price=22.99,
            stock=10
        )
    
    with pytest.raises(ValueError):
        product = Product(
            name="Camisa Nike",
            slug="Camisa-nike",
            price=22.99,
            stock=10
        )
        
def test_product_shcema_invalid_price():
    with pytest.raises(ValueError):
        product = Product(
            name="Camisa Nike",
            slug="camisa-nike",
            price=0,
            stock=10
        )