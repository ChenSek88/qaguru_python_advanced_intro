from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


app = FastAPI()


test_data = [
    {"id": 1, "name": "Ivan", "email": "ivan@gmail.com", "age": 22},
    {"id": 2, "name": "Alex", "email": "alex@gmail.com", "age": 25},
    {"id": 3, "name": "Bob", "email": "bob@gmail.com", "age": 29},
]


@app.get("/")
def root():
    return {"message": "FastAPI microservice"}


@app.get("/api/users/{user_id}")
def get_user(user_id: int):
    users = [user for user in test_data if user.get("id") == user_id]
    if not users: 
        raise HTTPException(status_code=404, detail="User not found")
    return users


@app.get("/api/users")
def get_users(): 
    return test_data


@app.put("/api/users/{user_id}")
def change_user_name(user_id: int, new_name: str):
    try:
        current_user = list(filter(lambda user: user.get("id") == user_id, test_data))[0]
        current_user["name"] = new_name
        return {"data": current_user}
    except IndexError: return {"status": 404, "error": "User not found"}


@app.delete("/api/users/{user_id}")
def delete_user(user_id: int):
    try: 
        user_index = next(index for index, user in enumerate(test_data) if user["id"] == user_id) 
        deleted_user = test_data.pop(user_index) 
        return {"data": deleted_user} 
    except StopIteration: return {"status": 404, "error": "User not found"}


@app.post("/api/users/")
def create_user(name: str, email: str, age: int):
    new_id = len(test_data) + 1 
    new_user = {"id": new_id, "name": name, "email": email, "age": age}
    test_data.append(new_user) 
    return {"data": new_user}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)