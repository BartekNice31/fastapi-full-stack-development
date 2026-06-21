from sqlalchemy.orm import Session
from schemas.user import UserCreate
from db.models.user import User
from core.hashing import Hasher

def create_new_user(user:User,db:Session):
    new_user=User(
        email=user.email
        ,password=Hasher.get_password_hash(user.password)
        ,is_active=True
        ,is_admin=False
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return user