from pydantic import BaseModel, EmailStr, HttpUrl


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