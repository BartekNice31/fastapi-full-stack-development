from pydantic import BaseModel,Field,validator
from typing import Optional,List
from enum import Enum
from datetime import datetime
import time

class Language(str,Enum):
    PYTHON="python"
    JAVA="java"
    C="c"
    CPLUSPLUS="c++"
    CSHARP="C#"

class Comment(BaseModel):
    text:Optional[str]=None

class Blog(BaseModel):
    title:str
    description:Optional[str]=None
    is_active:bool
    language:Language=Language.PYTHON
    comments:Optional[List[Comment]]
    created_at:datetime=Field(default_factory=datetime.now)

class CreateUser(BaseModel):
    email:str
    password:str
    confirm_password:str
    @validator("email")
    def validate_email(cls,value):
        if 'admin' in value:
            raise ValueError('this email is not allowed')
        return value

blog1=Blog(title="my first blog",is_active=True,comments=[{"text":"comment1"}])
print(blog1)

blog2=Blog(title="my second blog",is_active=True,comments=[Comment(text="my second comment")])
print(blog2)

comments=[Comment(text=f"comment {i}") for i in range(10)]
blog3=Blog(title="my third blog",is_active=True,comments=comments)

for c in blog3.comments:
    print(c)