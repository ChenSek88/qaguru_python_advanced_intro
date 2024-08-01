from pydantic import BaseModel, EmailStr, HttpUrl
from sqlmodel import Field, SQLModel


class UserDB(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    email: EmailStr
    first_name: str
    last_name: str
    avatar: str


class User(BaseModel):
    id: int
    email: EmailStr
    first_name: str
    last_name: str
    avatar: HttpUrl
    archive: bool


class UserCreate(BaseModel):
    email: EmailStr
    first_name: str
    last_name: str
    avatar: HttpUrl


class PaginationResponse(BaseModel):
    total: int
    page: int
    size: int
    pages: int
    items: list[User]


