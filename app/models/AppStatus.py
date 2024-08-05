from pydantic import BaseModel


class AppStatus(BaseModel):
    database: bool