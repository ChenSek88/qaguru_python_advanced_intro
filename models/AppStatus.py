from pydantic import BaseModel


class AppStatus(BaseModel):
    users: bool