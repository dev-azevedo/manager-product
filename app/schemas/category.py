import re
from pydantic import field_validator
from app.schemas.base import CustomBaseModel

class Category(CustomBaseModel):
    name: str
    slug: str
    
    @field_validator('slug')
    def validate_slug(cls, value):
        if not re.match('^([a-z]|[0-9]|-|_)+$', value):
            raise ValueError('Invalid slug')
        return value
    
class CategoryOutput(Category):
    id: int
    
    class Config:
        orm_mode=True