from datetime import datetime
from sqlalchemy import Column,Integer,String,Float,Boolean,DateTime,ForeignKey,Text
from sqlalchemy.orm import relationship

from db.base_class import Base

class User(Base):
    id=Column(Integer,primary_key=True,index=True)
    email=Column(String,nullable=False,index=True)
    password=Column(String,nullable=False)
    is_active=Column(Boolean,default=True)
    is_admin=Column(Boolean,default=False)
    blogs=relationship("Blog",back_populates="author")