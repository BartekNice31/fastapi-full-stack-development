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

def get_object_or_404(model:dict,id:str):
    object=model.get(str)
    if not object:
        raise HTTPException(detail=f"object about id={id} not founded",
                        status_code=status.HTTP_404_NOT_FOUND)
    return object

def get_blog_or_404(id:str):
    blog=blogs.get(id)
    if not blog:
        raise HTTPException(detail=f"blog about id={id} doesnt exist",
                        status_code=status.HTTP_404_NOT_FOUND)
    return blog

def user_name_or_404(id:str):
    user=users.get(id)
    if not user:
        raise HTTPException(detail=f"user about id={id} not founded",
                        status_code=status.HTTP_404_NOT_FOUND)
    return user

class GetObjectOr404:
    def __init__(self,model)->None:
        self.model=model
    def __call__(self,id:str):
        obj=self.model.get(id)
        if not obj:
            raise HTTPException(detail=f"Object about id={id} not founded"
                            ,status_code=status.HTTP_404_NOT_FOUND)
        return obj

app=FastAPI(title=settings.PROJECT_TITLE
        ,version=settings.PROJECT_VERSION)
# app=FastAPI(title="Dependiences of injections")

blog_dependency=GetObjectOr404(blogs)
@app.get("/Blog/{id}")
def get_blogs(blog_name:str=Depends(blog_dependency)):
    return blog_name
user_dependency=GetObjectOr404(users)
@app.get("/User/{id}")
def get_users(user_name:str=Depends(user_dependency)):
    return user_name