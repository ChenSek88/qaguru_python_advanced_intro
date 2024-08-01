from http import HTTPStatus
from app.models.User import UserDB, UserCreate
from typing import Iterable

from fastapi import APIRouter, HTTPException
from app.database import users
#from fastapi_pagination import Page, add_pagination, paginate


router = APIRouter(prefix="/api/users")

@router.get("/{user_id}", status_code=HTTPStatus.OK)
def get_user(user_id: int) -> UserDB:
    if user_id < 1:
        raise HTTPException(status_code=HTTPStatus.UNPROCESSABLE_ENTITY, detail="Invalid user id")
    user = users.get_user(user_id)

    if not user :
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="User not found")
    return user


@router.get("/", status_code=HTTPStatus.OK)
def get_users() -> Iterable[UserDB]:
    return users.get_users()

'''
@router.put("/{user_id}")
def change_user_name(user_id: int, new_name: str):
    user = user_get(user_id)
    user["first_name"] = new_name
    return {"data": user}


@router.delete("/{user_id}")
def delete_user_by_id(user_id: int):
    user = user_get(user_id)
    user["archive"] = True
    return {"data": user} 


@router.post("")
def create_user(user: UserCreate):
    new_id = len(users_db) + 1
    new_user = {
        "id": new_id, 
        "first_name": user.first_name, 
        "last_name": user.last_name, 
        "email": user.email, 
        "avatar": user.avatar,
        "archive": False
        }
    users_db.append(new_user)
    return {"data": new_user}'''