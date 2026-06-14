from pydantic import BaseModel,Field
from typing import Optional,List
from datetime import datetime
from enum import Enum

class Language(str,Enum):
    JAVA="java"
    PYTHON="python"
    C="c"
    CSHARP="C#"
    CPLUSPLUS="C++"

class Comment(BaseModel):
    text:Optional[str]=None

class Blog(BaseModel):
    title:str
    description:Optional[str]=None
    is_active:bool
    language:Language=Language.PYTHON
    comments:Optional[List[Comment]]
    created_at:datetime=Field(datetime.now)