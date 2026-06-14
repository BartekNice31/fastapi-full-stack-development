from fastapi import FastAPI,Depends,HTTPException,status
from config import settings

blogs={
    "1":"FastAPI Prerequisite"
    ,"2":"Building APIs with FastAPI"
    ,"3":"Background Tasks | Celery x FastAPI"
}

users={
    "8":"Jamie"
    ,"9":"Roman"
}

class GetObjectOr404:
    def __init__(self,model:dict)->None:
        self.model=model
    def __call__(self,id:str):
        obj=self.model.get(id)
        if obj is None:
            raise HTTPException(detail=f"object about id={id} not founded")
        return obj

app=FastAPI(title=settings.PROJECT_TITLE,version=settings.PROJECT_VERSION)

dependency_blog=GetObjectOr404(model=blogs)
dependency_user=GetObjectOr404(model=users)

@app.get("/")
def home():
    return "<h1>DEPENDENCIES TUTORIAL</h1>"
@app.get("/Blog/{id}")
def get_blogs(blog_name:str=Depends(dependency_blog)):
    return blog_name
@app.get("/User/{id}")
def get_users(user_name:str=Depends(dependency_user)):
    return user_name
