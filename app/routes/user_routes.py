from fastapi import APIRouter, Depends, Response, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.routes.deps import get_db_session
from app.schemas.user import User
from app.use_cases.user import UserUseCases


router = APIRouter(prefix="/user", tags=["User"])

@router.post("/register", status_code=status.HTTP_201_CREATED, description="Register new user")
def register_user(user: User, db_session: Session = Depends(get_db_session)):
    uc = UserUseCases(db_session)
    uc.register_user(user)
    return Response(status_code=status.HTTP_201_CREATED) 

@router.post("/login", status_code=status.HTTP_200_OK, description="Login user")
def user_login(form_data: OAuth2PasswordRequestForm = Depends(), db_session: Session = Depends(get_db_session)):
    uc = UserUseCases(db_session)
    
    user = User (username=form_data.username, password=form_data.password)
    
    token_data = uc.user_login(user=user, expires_in=60)
    
    return token_data