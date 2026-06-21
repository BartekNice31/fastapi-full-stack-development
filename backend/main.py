from fastapi import FastAPI
from datetime import datetime
from users import Users
from core.config import settings
from db.session import engine
from db.base import Base
from db.models import User, Blog
from apis.base import api_router
# class Settings:
#     PROJECT_NAME:str=''
#     PROJECT_VERSION:str='0.1.0'
# settings=Settings()
def include_router(app):
    app.include_router(api_router)
def create_tables():
    Base.metadata.create_all(bind=engine)
def start_application():
    app=FastAPI(title=settings.PROJECT_TITLE
        ,version=settings.PROJECT_VERSION) 
    include_router(app)
    #create_tables()
    return app

app=start_application()

blogs1=[
    {
        "id":1
        ,"title":"my first blog 😀"
        ,"time created":str(datetime.utcnow())
    },
    {
        "id":2
        ,"title":"my second blog 🐱"
        ,"time created":str(datetime.utcnow())
    },
]

@app.get("/")
def hello():
    return {"msg":"Hello FastAPI 🚀"}

@app.get("/test_blogs")
def test_blogs():
    return {"test blogs":blogs1}

users_test=Users

@app.get("/test_users")
def test_users():
    return {"users in test":users_test}