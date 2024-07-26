from pydantic import BaseModel


class User(BaseModel):
    id: int
    email: str
    name: str
    archive: bool


class UserCreate(BaseModel):
    email: str
    name: str