from fastapi import APIRouter, Depends, Response, status
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