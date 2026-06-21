from sqlalchemy.orm import Session
from db.models.blog import Blog
from core.hashing import Hasher
from schemas.blog import BlogCreate
from datetime import datetime
def create_new_blog(blog:BlogCreate,db:Session):
    new_blog=Blog(
        title=blog.title
        ,slug=blog.slug
        ,content=blog.content
        ,created_at=datetime.now()
        ,is_active=True
    )
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog