# pip install fastapi
# setting > projectName(자신의 프로젝트 폴더) > interpreter > fastapi 검색 후 설치
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

users = {
    0: {"userid": "apple", "name": "김사과"},
    1: {"userid": "banana", "name": "반하나"},
    2: {"userid": "orange", "name": "오렌지"},
    3: {"userid": "cherry", "name": "체리"},
}

# 비동기로 만드는 이유는 여러사람이 동시에 또는 따로 접속할 수 있기때문
# http://127.0.0.1:8000/
@app.get('/')
async def root():
    return {"message": "Hello FastAPI!"}

# http://127.0.0.1:8000/users/1
@app.get("/users/{id}")
async def find_user(id: int):
    user = users[id]
    return user

# http://127.0.0.1:8000/users/1/userid
# http://127.0.0.1:8000/users/1/name
@app.get("/users/{id}/{key}")
async def find_user_by_key(id: int, key: str):
    userid = users[id][key]
    return userid

class User(BaseModel):
    userid: str
    name: str

# http:127.0.0.1:8000/users/10
@app.post("/users/{id}")
async def create_user(id: int, user: User):
    if id in users:
        return {"error": "이미 존재하는 키"}
    users[id] = user.__dict__
    return {"success": "ok"}


# None이 나올 수 있을 때 Optional 사용, type check를 위함
class UserForUpdate(BaseModel):
    userid: Optional[str]
    name: Optional[str]

# 수정
@app.put("/users/{id}")
# id를 입력받아 id가 존재하지 않으면 에러
# userid가 존재하면 userid를 변경
# name이 존재하면 name을 변경
async def update_user(id: int, user: UserForUpdate):
    if id not in users:
        return {"error": "해당 id가 존재하지 않음"}
    if user.userid:
        users[id]["userid"] = user.userid
    if user.name:
        users[id]["name"] = user.name
    return {"success": "ok"}

# 삭제
@app.delete("/users/{id}")
# id를 입력받아 id가 존재하면 삭제
async def delete_user(id: int):
    if id not in users:
        return {"error": "해당 id가 존재하지 않음"}
    users.pop(id)
    return {"success": "ok"}


# uvicorn main:app --reload 터미널에 입력하여 실행