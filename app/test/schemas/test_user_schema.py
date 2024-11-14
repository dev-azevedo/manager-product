import pytest
from datetime import datetime
from app.schemas.user import User, TokenData

def test_user_schema():
    user = User(username="jhow", password="jhowPass")
    
    assert user.dict() == {
        "username": "jhow",
        "password": "jhowPass"
    }
    
def test_user_schema_invalid_username():
    with pytest.raises(ValueError):
        user = User(username="jhow#%!%", password="jhowPass")
    
    
def test_token_date():
    expire_at = datetime.now()
    token_data = TokenData(access_token='token teste', expires_at=expire_at)
    
    assert token_data.dict() == {
        "access_token": "token teste",
        "expires_at": expire_at
    }