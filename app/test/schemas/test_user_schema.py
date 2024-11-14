import pytest
from app.schemas.user import User

def test_user_schema():
    user = User(username="jhow", password="jhowPass")
    
    assert user.dict() == {
        "username": "jhow",
        "password": "jhowPass"
    }
    
def test_user_schema_invalid_username():
    with pytest.raises(ValueError):
        user = User(username="jhow#%!%", password="jhowPass")
    
    
