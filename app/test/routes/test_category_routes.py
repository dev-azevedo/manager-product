from fastapi.testclient import TestClient
from fastapi import status
from app.db.models import Category as CategoryModel
from app.main import app

client = TestClient(app)
headers = {'Authorization': 'Bearer Token'}
client.headers = headers

def test_add_category(db_session):
    body = {
        "name": "Roupa",
        "slug": "roupa"
    }
    
    response = client.post("/categories/add", json=body)
    
    assert response.status_code == status.HTTP_201_CREATED
    
    categories_on_db = db_session.query(CategoryModel).all()
    assert len(categories_on_db) == 1
    db_session.delete(categories_on_db[0])
    db_session.commit()
    
def test_list_categories(categories_on_db):
    response = client.get("/categories/list")
    
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert len(data) == 4
    assert data[0] == {
        "name": categories_on_db[0].name,
        "slug": categories_on_db[0].slug,
        "id": categories_on_db[0].id
    }
    
def test_delete_category(db_session):
    category_model = CategoryModel(
        name="Roupa",
        slug="roupa"
    )
    db_session.add(category_model)
    db_session.commit()
    
    response = client.delete(f"/categories/delete/{category_model.id}")
    
    assert response.status_code == status.HTTP_200_OK
    
    category_model = db_session.query(CategoryModel).first()
    assert category_model is None