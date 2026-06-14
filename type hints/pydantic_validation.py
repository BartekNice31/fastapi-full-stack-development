from pydantic import BaseModel,Field,validator,root_validator,model_validator
from typing import Optional,List
from datetime import datetime
import time

class CreateUser(BaseModel):
    email:str
    password:str
    confirm_password:str

    @validator("email")
    def validate_email(cls,value):
        if 'admin' in value:
            raise ValueError("This email is not allowed")
        if not '@' in value:
            raise ValueError("This email without @ is not allowed")
        return value
    
    @model_validator(mode="after")
    def validate_passwords(self):
        if self.password!=self.confirm_password:
            raise ValueError("passwords do not match")
        return self
    
CreateUser(email="barto@wp.pl",password="111",confirm_password="111")