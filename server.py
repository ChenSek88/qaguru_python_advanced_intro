from fastapi import FastAPI, HTTPException


app = FastAPI()


test_data = {
    1: {"id": 1, "name": "Ivan", "email": "ivan@gmail.com", "age": 22, "archive": False},
    2: {"id": 2, "name": "Alex", "email": "alex@gmail.com", "age": 25, "archive": False},
    3: {"id": 3, "name": "Bob", "email": "bob@gmail.com", "age": 29, "archive": False},
    4: {"id": 4, "name": "Alice", "email": "alice@gmail.com", "age": 20, "archive": False}
}


def user_get(user_id: int):
    if user_id in test_data and not test_data[user_id].get("archive"):
        return test_data[user_id]
    raise HTTPException(status_code=404, detail="User not found")


@app.get("/")
def root():
    return {"message": "FastAPI microservice"}


@app.get("/api/users/{user_id}")
def get_user_by_id(user_id: int):
    return user_get(user_id)    
    

@app.get("/api/users")
def get_non_archived_users(): 
    users = [user for user in test_data.values() if not user.get("archive")] 
    return users


@app.put("/api/users/{user_id}")
def change_user_name(user_id: int, new_name: str):
    user = user_get(user_id)
    user["name"] = new_name
    return {"data": user}


@app.delete("/api/users/{user_id}")
def delete_user_by_id(user_id: int):
    user = user_get(user_id)
    user["archive"] = True
    return {"data": user} 


@app.post("/api/users")
def create_user(name: str, email: str, age: int):
    new_id = len(test_data) + 1
    new_user = {"id": new_id, "name": name, "email": email, "age": age, "archive": False}
    test_data[new_id] = new_user
    return {"data": new_user}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app)