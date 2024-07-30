from fastapi import FastAPI, HTTPException
from models.User import User, UserCreate
from models.AppStatus import AppStatus
from http import HTTPStatus
import json
from fastapi_pagination import Page, add_pagination, paginate


app = FastAPI()
add_pagination(app)

users: list[User] = []


def user_get(user_id: int):
    non_arch_users = [user for user in users if not user.get("archive")]     
    if user_id < 1:
        raise HTTPException(status_code=HTTPStatus.UNPROCESSABLE_ENTITY, detail="Invalid user id")
    if user_id > len(users):
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="User not found")
    return non_arch_users[user_id - 1]


@app.get("/", status_code=HTTPStatus.OK)
def root():
    return {"message": "FastAPI microservice is running"}


@app.get("/status", status_code=HTTPStatus.OK)
def status() -> AppStatus:
    return AppStatus(users=bool(users))


@app.get("/api/users/{user_id}")
def get_user_by_id(user_id: int):
    return user_get(user_id)    
    

@app.get("/api/users")
def get_non_archived_users() -> Page[User]: 
    non_archived_users = [user for user in users if not user.get("archive")] 
    return paginate(non_archived_users)
    

@app.put("/api/users/{user_id}")
def change_user_name(user_id: int, new_name: str):
    user = user_get(user_id)
    user["first_name"] = new_name
    return {"data": user}


@app.delete("/api/users/{user_id}")
def delete_user_by_id(user_id: int):
    user = user_get(user_id)
    user["archive"] = True
    return {"data": user} 


@app.post("/api/users")
def create_user(user: UserCreate):
    new_id = len(users) + 1
    new_user = {
        "id": new_id, 
        "first_name": user.first_name, 
        "last_name": user.last_name, 
        "email": user.email, 
        "avatar": user.avatar,
        "archive": False
        }
    users.append(new_user)
    return {"data": new_user}


with open("users.json") as f:
    users = json.load(f)

    
for user in users:
    User.model_validate(user)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app)