import pytest
from fastapi.exception_handlers import HTTPException
from app.use_cases.category import CategoryUseCases
from app.db.models import Category as CategoryModel
from app.schemas.category import Category, CategoryOutput

def test_add_category_uc(db_session):
    uc = CategoryUseCases(db_session)
    
    category = Category(
        name="Roupa",
        slug="roupa"
    )
    
    uc.add_category(category=category)
    
    category_on_db = db_session.query(CategoryModel).all()
    
    assert len(category_on_db) == 1
    assert category_on_db[0].name == category.name
    assert category_on_db[0].slug == category.slug
    
    db_session.delete(category_on_db[0])
    db_session.commit()
    
def test_list_categories_uc(db_session, categories_on_db):
    uc = CategoryUseCases(db_session)
    
    categories = uc.list_categories()
    
    assert len(categories) == len(categories_on_db)
    assert type(categories[0]) == CategoryOutput
    assert categories[0].id == categories_on_db[0].id
    assert categories[0].name == categories_on_db[0].name
    assert categories[0].slug == categories_on_db[0].slug
    
def test_delete_category_uc(db_session):
    category_model = CategoryModel(
        name="Roupa",
        slug="roupa"
    )
    db_session.add(category_model)
    db_session.commit()
    
    uc = CategoryUseCases(db_session=db_session)
    
    uc.delete_category(id=category_model.id)    
    
    category_model = db_session.query(CategoryModel).first()
    assert category_model is None
   
def test_delete_category_non_exist(db_session):    
    uc = CategoryUseCases(db_session)
    
    with pytest.raises(HTTPException):
        uc.delete_category(1)    
   
    