from pydantic import BaseModel,Field,validator,model_validator,root_validator
from typing import Optional,List
from datetime import datetime

class CreateUser(BaseModel):
    email:str
    password:str
    confirm_password:str
    @validator("email")
    def validate_email(cls,value):
        if 'admin' in value:
            raise ValueError("This email is not allowed")
        return value
    @root_validator(skip_on_failure=True)
    def validate_passwords_v1(cls,values):
        password=values.get("password")
        confirm_password=values.get("confirm_password")
        if password!=confirm_password:
            raise ValueError("Passwords do not match")
        return values
    @model_validator(mode="after")
    def validate_passwords(self):
        if self.password!=self.confirm_password:
            raise ValueError("These passwords do not match")
        return self
    
print(CreateUser(email="barto@wp.pl",password="111",confirm_password="111"))