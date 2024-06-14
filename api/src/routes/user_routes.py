from fastapi import APIRouter
from services.users_service import UserService

router = APIRouter()
user_service = UserService()


@router.get('/')
def get_users():
    return user_service.get_users()
