from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


app = FastAPI()


test_data = [
    {"id": 1, "name": "Ivan", "email": "ivan@gmail.com", "age": 22, "archive": False},
    {"id": 2, "name": "Alex", "email": "alex@gmail.com", "age": 25, "archive": False},
    {"id": 3, "name": "Bob", "email": "bob@gmail.com", "age": 29, "archive": False},
    {"id": 4, "name": "Alice", "email": "alice@gmail.com", "age": 20, "archive": False}
]


@app.get("/")
def root():
    return {"message": "FastAPI microservice"}


@app.get("/api/users/{user_id}")
def get_user(user_id: int):
    users = [user for user in test_data if user.get("id") == user_id and user.get("archive") is False]
    if not users: 
        raise HTTPException(status_code=404, detail="User not found")
    return users


@app.get("/api/users")
def get_users(): 
    users = [user for user in test_data if user.get("archive") is False]
    return users


@app.put("/api/users/{user_id}")
def change_user_name(user_id: int, new_name: str):
    test_data_idx = {user["id"]: user for user in test_data}
    if not user_id in test_data_idx:
        raise HTTPException(status_code=404, detail="User not found")
    test_data_idx[user_id]["name"] = new_name
    return {"data": test_data_idx[user_id]}


@app.delete("/api/users/{user_id}")
def delete_user(user_id: int):
    test_data_idx = {user["id"]: user for user in test_data}
    if not user_id in test_data_idx:
        raise HTTPException(status_code=404, detail="User not found")
    deleted_user = test_data_idx[user_id]
    deleted_user.update({"archive": True})
    return {"data": deleted_user} 


@app.post("/api/users")
def create_user(name: str, email: str, age: int):
    new_id = len(test_data) + 1
    new_user = {"id": new_id, "name": name, "email": email, "age": age, "archive": False}
    test_data.append(new_user) 
    return {"data": new_user}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)