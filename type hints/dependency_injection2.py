from fastapi import FastAPI,HTTPException,status,Depends
from datetime import datetime
from fastapi.testclient import TestClient

development_db=["DB for development"]
users_db=["user1"]
comments_db=[f"comment1-:-{datetime.now()}"]

def get_db_session():
    return development_db

def get_db_users():
    return users_db

def get_db_comments():
    return comments_db

app=FastAPI()

client=TestClient(app=app)

def test_item_should_add_to_database():
    response=client.get("/items/?item=sugar")
    assert response.status_code==200
    assert response.text=='{"message":"sugar added"}'

@app.post("/items")
def add_item(item:str,db=Depends(get_db_session)):
    db.append(item)
    print(db)
    return {"message":f"item: {item} added"}

@app.post("/users")
def add_user(new_user:str,db=Depends(get_db_users)):
    db.append(new_user)
    print(db)
    return {"message":f"new user added: {new_user}"}

@app.post("/comments")
def add_comment(new_comment:str,db=Depends(get_db_comments)):
    db.append(f"{new_comment}-:-{datetime.now()}")
    print(db)
    return {"message":f"new comment added: {new_comment}"}