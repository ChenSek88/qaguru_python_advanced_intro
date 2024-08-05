from http import HTTPStatus

from fastapi import APIRouter

from app.models.AppStatus import AppStatus
from app.database.engine import check_availability


router = APIRouter()


@router.get("/status", status_code=HTTPStatus.OK)
def status() -> AppStatus:
    return AppStatus(database=check_availability())