from typing import Iterable

from sqlmodel import Session, select
from app.database.engine import engine
from app.models.User import UserDB



def get_user(user_id: int) -> UserDB | None:
    with Session(engine) as session:
        return session.get(UserDB, user_id)


def get_users() -> Iterable[UserDB]:
    with Session(engine) as session:
        statement = select(UserDB)
        return session.exec(statement).all()