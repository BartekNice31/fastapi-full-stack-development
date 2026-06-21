from pydantic import BaseModel,Field,EmailStr
from datetime import datetime,timezone
class BlogCreate(BaseModel):
    title:str=Field(...,min_length=4)
    slug:str=Field(...,min_length=4)
    content:str=Field(...,min_length=10)
    created_at:datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    is_active:bool
