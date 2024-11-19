from fastapi.testclient import TestClient
from fastapi import status
from app.schemas.user import User
from app.db.models import User as UserModel
from app.main import app

client = TestClient(app)

def test_register_user_route(db_session):
    body = {
        "username": "jhow",
        "password": "jhowPass"
    }
    
    response = client.post("/user/register", json=body)
    assert response.status_code == status.HTTP_201_CREATED
    
    user_on_db = db_session.query(UserModel).first()
    
    assert user_on_db is not None
    
    db_session.delete(user_on_db)
    db_session.commit()
    
def test_register_user_route_user_already_exists(db_session, user_on_db):
    body = {
        "username": user_on_db.username,
        "password": "jhowPass"
    }
    
    response = client.post("/user/register", json=body)
    assert response.status_code == status.HTTP_400_BAD_REQUEST

def test_user_login_route(db_session, user_on_db):
    body = {
        "username": user_on_db.username,
        "password": "jhowPass"
    }
    
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    
    response = client.post("/user/login", data=body, headers=headers)
    
    assert response.status_code == status.HTTP_200_OK
    
    data = response.json()
    
    assert "access_token" in data
    assert "expires_at" in data
    
def test_user_login_route_invalid_username(db_session, user_on_db):
    body = {
        "username": 'invalid',
        "password": "jhowPass"
    }
    
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    
    response = client.post("/user/login", data=body, headers=headers)
    
    assert response.status_code == status.HTTP_401_UNAUTHORIZED
    
def test_user_login_route_invalid_password(db_session, user_on_db):
    body = {
        "username": user_on_db.username,
        "password": "invalid"
    }
    
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    
    response = client.post("/user/login", data=body, headers=headers)
    
    assert response.status_code == status.HTTP_401_UNAUTHORIZED